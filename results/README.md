# Results

This folder contains the computational result files for the Bin Packing Problem with Setups and Conflicts (BPPSC).

The results are organized by conflict density.

## Structure

| Folder | Description |
|---|---|
| `by_density/` | Full Excel result files for each conflict-density level |
| `by_problem_size/` | Optional summaries grouped by number of items |

## Density-level result files

For each conflict density `rho = 0.0, 0.1, ..., 0.9`, the corresponding folder contains:

| File | Description |
|---|---|
| `benchmark_comparison_rho_0.X.xlsx` | Comparison between MSIG and adapted benchmark algorithms |
| `msig_vs_lower_bound_rho_0.X.xlsx` | Comparison between MSIG and the proposed lower bound |

For `rho = 0.0`, the folder also contains:

| File | Description |
|---|---|
| `comparison_with_best_known_BPPS.xlsx` | Comparison between MSIG and the BPPS best-known solutions |

## Compared algorithms

The benchmark-comparison files compare the following algorithms:

- P-FFD
- P-BFD
- P-WFD
- Best C-TP
- MSIG

## Note

The source codes of MSIG and the adapted benchmark algorithms are not included in this repository at this stage. This repository provides the benchmark instances, conflict-generation code, and computational result files.
