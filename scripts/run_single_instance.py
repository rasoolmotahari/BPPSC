"""
Run one BPPSC algorithm on one instance.

Example:
python scripts/run_single_instance.py --instance data/toy_example/toy_bppsc_instance.txt --algorithm msig
"""

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True, help="Path to the instance file")
    parser.add_argument(
        "--algorithm",
        required=True,
        help="Algorithm name: msig, p_ffd, p_bfd, p_wfd, c_tp_ffd, c_tp_bfd",
    )
    args = parser.parse_args()

    print(f"Instance: {args.instance}")
    print(f"Algorithm: {args.algorithm}")
    print("This script will call the selected algorithm after the implementation is added.")


if __name__ == "__main__":
    main()
