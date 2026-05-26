"""
Run all BPPSC instances for one conflict density.

Example:
python scripts/run_all_by_density.py --rho 0.4
"""

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rho", required=True, help="Conflict density, e.g., 0.4")
    args = parser.parse_args()

    print(f"Running all instances for rho = {args.rho}")
    print(f"Input folder: data/bppsc_instances/rho_{args.rho}/")
    print(f"Output folder: results/by_density/rho_{args.rho}/")


if __name__ == "__main__":
    main()
