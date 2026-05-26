# BPPSC

This repository contains benchmark instances, algorithms, and computational results for the **Bin Packing Problem with Setups and Conflicts (BPPSC)**.

The BPPSC extends the classical Bin Packing Problem by considering:

1. setup classes,
2. setup capacity consumption,
3. setup costs,
4. pairwise item conflicts.

The proposed solution method is a **Multi-Start Iterated Greedy (MSIG)** algorithm.

> This repository is currently private and will be made public after the paper submission/review process.

## Repository structure

| Folder | Description |
|---|---|
| `data/` | BPPS base instances, generated BPPSC instances, and toy examples |
| `src/` | Python implementation of MSIG, lower bound, conflict generation, and benchmark algorithms |
| `scripts/` | Scripts for running experiments and reproducing tables |
| `results/` | Computational results separated by density, problem size, and paper tables |
| `docs/` | Documentation for instance format, result format, algorithm, and reproduction |
| `figures/` | Figures used to summarize computational results |

## Benchmark instances

The benchmark set contains ten conflict-density levels.

| Conflict density | Number of instances | Folder |
|---:|---:|---|
| 0.0 | 480 | `data/bppsc_instances/rho_0.0/` |
| 0.1 | 480 | `data/bppsc_instances/rho_0.1/` |
| 0.2 | 480 | `data/bppsc_instances/rho_0.2/` |
| 0.3 | 480 | `data/bppsc_instances/rho_0.3/` |
| 0.4 | 480 | `data/bppsc_instances/rho_0.4/` |
| 0.5 | 480 | `data/bppsc_instances/rho_0.5/` |
| 0.6 | 480 | `data/bppsc_instances/rho_0.6/` |
| 0.7 | 480 | `data/bppsc_instances/rho_0.7/` |
| 0.8 | 480 | `data/bppsc_instances/rho_0.8/` |
| 0.9 | 480 | `data/bppsc_instances/rho_0.9/` |

Total number of generated BPPSC instances: **4,800**.

## Algorithms

The repository includes the following algorithms:

| Algorithm | Description |
|---|---|
| `MSIG` | Proposed Multi-Start Iterated Greedy algorithm |
| `P-FFD` | Parametric First-Fit Decreasing heuristic |
| `P-BFD` | Parametric Best-Fit Decreasing heuristic |
| `P-WFD` | Parametric Worst-Fit Decreasing heuristic |
| `C-TP-FFD` | Conflict-aware two-phase BPPS benchmark using FFD |
| `C-TP-BFD` | Conflict-aware two-phase BPPS benchmark using BFD |

## Main computational comparisons

The paper reports three main computational comparisons:

1. MSIG versus reported BPPS best-known solutions for conflict-free instances.
2. MSIG versus the proposed lower bound.
3. MSIG versus adapted benchmark algorithms.

Detailed results are stored in:

- `results/by_density/`
- `results/by_problem_size/`
- `results/tables_for_paper/`

## Reproducing the experiments

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run one toy instance:

```bash
python scripts/run_single_instance.py --instance data/toy_example/toy_bppsc_instance.txt --algorithm msig
```

Run all instances for one density:

```bash
python scripts/run_all_by_density.py --rho 0.4
```

Reproduce all paper tables:

```bash
python scripts/reproduce_tables.py
```

## Citation

Citation information will be added after publication.
