# Results

This folder contains the computational results for the Bin Packing Problem with Setups and Conflicts (BPPSC).

The results are organized by conflict density. The benchmark set includes ten conflict-density levels, with 576 instances at each level and 5,760 instances in total.

## Structure

| Folder        | Description |
| ------------- | ----------- |
| `by_density/` | Computational result files for each conflict-density level |

## Density-level result files

For each conflict density `rho = 0.0, 0.1, ..., 0.9`, the corresponding folder contains:

| File                                | Description |
| ----------------------------------- | ----------- |
| `benchmark_comparison_rho_0.X.xlsx` | Comparison of MSIG with the adapted benchmark algorithms for all 576 instances |
| `msig_vs_lower_bound_rho_0.X.xlsx`  | Comparison of MSIG solutions with the proposed lower bound for all 576 instances |

For `rho = 0.0`, the folder also contains:

| File                                   | Description |
| -------------------------------------- | ----------- |
| `comparison_with_best_known_BPPS.xlsx` | Comparison of MSIG with the reported BPPS best-known solutions for the 576 conflict-free instances |

## Compared algorithms

The benchmark-comparison files include:

- P-FFD
- P-BFD
- P-WFD
- Best C-TP
- MSIG

## Result organization

The density-specific folders are:

- `rho_0.0/`
- `rho_0.1/`
- `rho_0.2/`
- `rho_0.3/`
- `rho_0.4/`
- `rho_0.5/`
- `rho_0.6/`
- `rho_0.7/`
- `rho_0.8/`
- `rho_0.9/`

Each folder contains results for 576 BPPSC instances at the corresponding conflict-density level.

## Note

The result files provide the computational comparisons of MSIG with the adapted benchmark algorithms and the proposed lower bound. For the conflict-free instances (`rho = 0.0`), an additional file compares MSIG with the reported BPPS best-known solutions.
