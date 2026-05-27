#!/usr/bin/env python3
"""
Add conflicts to existing BPPS/BPPSC .txt instances.

How to use:
-----------
Put this Python file in the same folder as your .txt data files and run it.

Default behavior:
    - Reads all .txt files from the same folder as this script.
    - Creates a new folder named "instances_with_conflicts".
    - Writes new files with generated conflicts into that new folder.
    - Keeps the original filenames unchanged.
    - Keeps the original header, setup data, item counts, and item weights unchanged.
    - Adds conflict IDs in front of each item weight row exactly like:
          item_weight conflicting_item_1 conflicting_item_2 ...

Example:
    python add_conflicts_to_existing_bppsc_same_folder.py

The conflict density is fixed to 0.1.

Example with another output folder:
    python add_conflicts_to_existing_bppsc_fixed_c10_same_names.py --output-dir "my_new_conflict_data"
"""

import argparse
import csv
import hashlib
import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


@dataclass
class ClassData:
    """Data of one setup class."""
    setup_cost: int
    setup_weight: int
    item_count: int


@dataclass
class InstanceData:
    """Parsed data of one existing instance."""
    source_file: str
    n: int
    m: int
    bin_capacity: int
    bin_cost: int
    classes: List[ClassData]
    item_weights: List[int]
    existing_conflicts: Dict[int, List[int]]


def parse_instance_file(filepath: Path) -> InstanceData:
    """
    Read one existing .txt instance.

    Expected format:
        line 1: n  m  bin_capacity  bin_cost
        next m lines: setup_cost  setup_weight  item_count
        next n lines: item_weight [optional conflict IDs...]

    Notes:
        - Existing conflict IDs, if present, are read.
        - By default, the script replaces them with newly generated conflicts.
        - Use --keep-existing-conflicts if you want to keep and merge them.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        raw_lines = [line.strip() for line in file if line.strip()]

    if not raw_lines:
        raise ValueError(f"File is empty: {filepath}")

    header = raw_lines[0].split()
    if len(header) < 4:
        raise ValueError(
            f"Invalid header in {filepath}. Expected: n m bin_capacity bin_cost"
        )

    n = int(header[0])
    m = int(header[1])
    bin_capacity = int(header[2])
    bin_cost = int(header[3])

    expected_lines = 1 + m + n
    if len(raw_lines) < expected_lines:
        raise ValueError(
            f"File {filepath} has {len(raw_lines)} non-empty lines, "
            f"but expected at least {expected_lines} lines."
        )

    classes: List[ClassData] = []
    for idx in range(1, 1 + m):
        parts = raw_lines[idx].split()
        if len(parts) < 3:
            raise ValueError(
                f"Invalid setup-class line {idx + 1} in {filepath}. "
                f"Expected: setup_cost setup_weight item_count"
            )

        classes.append(
            ClassData(
                setup_cost=int(parts[0]),
                setup_weight=int(parts[1]),
                item_count=int(parts[2]),
            )
        )

    item_weights: List[int] = []
    existing_conflicts: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}

    item_start = 1 + m
    for local_idx in range(n):
        item_id = local_idx + 1
        line_index = item_start + local_idx
        parts = raw_lines[line_index].split()

        if not parts:
            raise ValueError(f"Empty item line in {filepath}, item {item_id}.")

        item_weight = int(parts[0])
        item_weights.append(item_weight)

        if len(parts) > 1:
            conflicts = [int(x) for x in parts[1:]]
            existing_conflicts[item_id] = conflicts

    total_items_from_classes = sum(cls.item_count for cls in classes)
    if total_items_from_classes != n:
        print(
            f"Warning: In {filepath.name}, sum of class item counts "
            f"({total_items_from_classes}) is not equal to n ({n})."
        )

    return InstanceData(
        source_file=str(filepath),
        n=n,
        m=m,
        bin_capacity=bin_capacity,
        bin_cost=bin_cost,
        classes=classes,
        item_weights=item_weights,
        existing_conflicts=existing_conflicts,
    )


def threshold_suffix(conflict_density: float) -> str:
    """Convert 0.1 to 10, 0.25 to 25, etc."""
    return str(int(round(conflict_density * 100)))


def stable_conflict_seed(filename: str, base_seed: int) -> int:
    """
    Create a deterministic seed from the filename and base seed.

    This avoids Python's built-in hash(), which may change between runs.
    """
    key = f"{filename}|{base_seed}".encode("utf-8")
    digest = hashlib.sha256(key).hexdigest()
    return int(digest[:12], 16)


def generate_conflicts(
    n: int,
    conflict_density: float,
    rng: random.Random,
) -> Dict[int, Set[int]]:
    """
    Generate one-directional conflict lists.

    For each unordered pair (i, j), i < j:
        draw u ~ U(0,1)
        if u < conflict_density, add j to the conflict list of item i

    This is the same reporting style as your previous generator:
        item i row reports only conflict IDs greater than i.
    """
    conflicts: Dict[int, Set[int]] = {i: set() for i in range(1, n + 1)}

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            u = rng.random()
            if u < conflict_density:
                conflicts[i].add(j)

    return conflicts


def merge_existing_conflicts(
    generated_conflicts: Dict[int, Set[int]],
    existing_conflicts: Dict[int, List[int]],
    n: int,
) -> Dict[int, Set[int]]:
    """
    Merge existing conflict lists with generated conflicts.

    The final stored format remains one-directional:
        if pair (i, j) is a conflict and i < j, write j in row i.
    """
    merged: Dict[int, Set[int]] = {i: set(generated_conflicts[i]) for i in range(1, n + 1)}

    for i, conflict_list in existing_conflicts.items():
        for j in conflict_list:
            if i == j:
                continue
            a, b = min(i, j), max(i, j)
            if 1 <= a <= n and 1 <= b <= n:
                merged[a].add(b)

    return merged


def count_conflict_edges(conflicts: Dict[int, Set[int]]) -> int:
    """Count one-directional stored conflict edges."""
    return sum(len(values) for values in conflicts.values())


def write_instance_file(
    instance: InstanceData,
    output_path: Path,
    conflicts: Dict[int, Set[int]],
) -> None:
    """Write the new BPPSC instance with conflicts."""
    with open(output_path, "w", encoding="utf-8") as file:
        # Header
        file.write(
            f"{instance.n}\t{instance.m}\t"
            f"{instance.bin_capacity}\t{instance.bin_cost}\n"
        )

        # Setup-class lines
        for cls in instance.classes:
            file.write(
                f"{cls.setup_cost}\t{cls.setup_weight}\t{cls.item_count}\n"
            )

        # Item lines
        for item_id, item_weight in enumerate(instance.item_weights, start=1):
            conflict_items = sorted(conflicts[item_id])

            if conflict_items:
                conflicts_text = " ".join(str(j) for j in conflict_items)
                file.write(f"{item_weight} {conflicts_text}\n")
            else:
                file.write(f"{item_weight}\n")


def build_output_filename(input_file: Path, conflict_density: float) -> str:
    """
    Keep the original filename for the generated instance.

    Example:
        original file: instance_01.txt
        output file  : instance_01.txt

    Since the output files are written to a separate output folder, the original
    files are not overwritten.
    """
    return input_file.name


def collect_txt_files(input_dir: Path, recursive: bool) -> List[Path]:
    """Collect .txt files from the input folder."""
    if recursive:
        files = sorted(input_dir.rglob("*.txt"))
    else:
        files = sorted(input_dir.glob("*.txt"))

    return [f for f in files if f.is_file()]


def create_reports(
    output_dir: Path,
    summary_rows: List[Dict[str, object]],
    detailed_report: List[Dict[str, object]],
    write_detailed_report: bool,
) -> None:
    """Create CSV and JSON reports."""
    summary_path = output_dir / "conflict_generation_summary.csv"

    if summary_rows:
        fieldnames = list(summary_rows[0].keys())
        with open(summary_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(summary_rows)

    if write_detailed_report:
        detailed_path = output_dir / "conflict_generation_detailed_report.json"
        with open(detailed_path, "w", encoding="utf-8") as file:
            json.dump(detailed_report, file, indent=2)


def add_conflicts_to_folder(
    input_dir: Path,
    output_dir: Path,
    densities: List[float],
    seed: int,
    recursive: bool,
    keep_existing_conflicts: bool,
    write_detailed_report: bool,
) -> None:
    """Main processing function."""
    output_dir.mkdir(parents=True, exist_ok=True)

    txt_files = collect_txt_files(input_dir=input_dir, recursive=recursive)

    # Do not read files from the output folder if recursive mode is used.
    output_dir_resolved = output_dir.resolve()
    filtered_files = []
    for file in txt_files:
        try:
            file.resolve().relative_to(output_dir_resolved)
            continue
        except ValueError:
            filtered_files.append(file)

    txt_files = filtered_files

    if not txt_files:
        print(f"No .txt files found in: {input_dir}")
        return

    print("Starting conflict generation for existing data...")
    print(f"Input folder : {input_dir}")
    print(f"Output folder: {output_dir}")
    print(f"Densities    : {densities}")
    print(f"Seed         : {seed}")
    print(f"Files found  : {len(txt_files)}")
    print("-" * 70)

    summary_rows: List[Dict[str, object]] = []
    detailed_report: List[Dict[str, object]] = []

    generated_file_count = 0

    for file_index, input_file in enumerate(txt_files, start=1):
        try:
            instance = parse_instance_file(input_file)
        except Exception as exc:
            print(f"✗ Skipped {input_file.name}: {exc}")
            continue

        # Same base file gets the same pairwise random stream for all densities.
        # This makes c10, c20, c30, ... directly comparable.
        conflict_seed = stable_conflict_seed(input_file.name, seed)

        total_possible_pairs = instance.n * (instance.n - 1) // 2

        print(f"Reading file {file_index}/{len(txt_files)}: {input_file.name}")
        print(
            f"  n={instance.n}, m={instance.m}, "
            f"capacity={instance.bin_capacity}, bin_cost={instance.bin_cost}"
        )

        for density in densities:
            if not (0.0 <= density <= 1.0):
                raise ValueError(f"Conflict density must be in [0,1], got {density}")

            rng = random.Random(conflict_seed)
            generated_conflicts = generate_conflicts(
                n=instance.n,
                conflict_density=density,
                rng=rng,
            )

            if keep_existing_conflicts:
                final_conflicts = merge_existing_conflicts(
                    generated_conflicts=generated_conflicts,
                    existing_conflicts=instance.existing_conflicts,
                    n=instance.n,
                )
            else:
                final_conflicts = generated_conflicts

            edge_count = count_conflict_edges(final_conflicts)
            realized_density = (
                edge_count / total_possible_pairs if total_possible_pairs > 0 else 0.0
            )

            output_filename = build_output_filename(input_file, density)
            output_path = output_dir / output_filename

            write_instance_file(
                instance=instance,
                output_path=output_path,
                conflicts=final_conflicts,
            )

            generated_file_count += 1

            summary_rows.append(
                {
                    "source_file": input_file.name,
                    "output_file": output_filename,
                    "n": instance.n,
                    "m": instance.m,
                    "bin_capacity": instance.bin_capacity,
                    "bin_cost": instance.bin_cost,
                    "target_conflict_density": density,
                    "number_of_conflict_edges": edge_count,
                    "total_possible_pairs": total_possible_pairs,
                    "realized_conflict_density": round(realized_density, 6),
                    "keep_existing_conflicts": keep_existing_conflicts,
                }
            )

            if write_detailed_report:
                detailed_report.append(
                    {
                        "source_file": input_file.name,
                        "output_file": output_filename,
                        "header": {
                            "n": instance.n,
                            "m": instance.m,
                            "bin_capacity": instance.bin_capacity,
                            "bin_cost": instance.bin_cost,
                        },
                        "classes": [asdict(cls) for cls in instance.classes],
                        "item_weights": instance.item_weights,
                        "target_conflict_density": density,
                        "number_of_conflict_edges": edge_count,
                        "total_possible_pairs": total_possible_pairs,
                        "realized_conflict_density": realized_density,
                        "conflicts": {
                            str(i): sorted(list(final_conflicts[i]))
                            for i in range(1, instance.n + 1)
                        },
                    }
                )

            print(
                f"  ✓ density={density:.2f} -> {output_filename} "
                f"edges={edge_count}, realized_density={realized_density:.4f}"
            )

    create_reports(
        output_dir=output_dir,
        summary_rows=summary_rows,
        detailed_report=detailed_report,
        write_detailed_report=write_detailed_report,
    )

    print("-" * 70)
    print("Completed.")
    print(f"Generated files: {generated_file_count}")
    print(f"Summary report : {output_dir / 'conflict_generation_summary.csv'}")
    if write_detailed_report:
        print(f"Detailed report: {output_dir / 'conflict_generation_detailed_report.json'}")


def main() -> None:
    script_folder = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description=(
            "Read existing BPPS/BPPSC .txt files and add conflict lists to item rows. "
            "Conflict density is fixed to 0.1. If no input/output folders are given, "
            "the script reads from the same folder where this .py file is located "
            "and writes to a new subfolder."
        )
    )

    parser.add_argument(
        "--input-dir",
        "-i",
        type=str,
        default=None,
        help=(
            "Folder containing the original .txt data. "
            "Default: the same folder as this Python script."
        ),
    )

    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default=None,
        help=(
            "Folder for the generated data with conflicts. "
            "Default: a subfolder named 'instances_with_conflicts' inside the input folder."
        ),
    )

    parser.add_argument(
        "--seed",
        "-s",
        type=int,
        default=0,
        help="Base random seed. Default: 0.",
    )

    parser.add_argument(
        "--keep-existing-conflicts",
        action="store_true",
        help=(
            "If the input files already contain conflicts, keep them and add new ones. "
            "Default: replace existing conflict lists."
        ),
    )

    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Read .txt files from subfolders too. Default: only the main folder.",
    )

    parser.add_argument(
        "--no-detailed-report",
        action="store_true",
        help="Do not write the detailed JSON report.",
    )

    args = parser.parse_args()

    if args.input_dir is None:
        input_dir = script_folder
    else:
        input_dir = Path(args.input_dir).resolve()

    if args.output_dir is None:
        output_dir = input_dir / "instances_with_conflicts"
    else:
        output_dir = Path(args.output_dir).resolve()

    if input_dir.resolve() == output_dir.resolve():
        raise ValueError(
            "The output folder must be different from the input folder, "
            "because output files keep the same filenames as the original files."
        )

    add_conflicts_to_folder(
        input_dir=input_dir,
        output_dir=output_dir,
        densities=[0.5],
        seed=args.seed,
        recursive=args.recursive,
        keep_existing_conflicts=args.keep_existing_conflicts,
        write_detailed_report=not args.no_detailed_report,
    )


if __name__ == "__main__":
    main()
