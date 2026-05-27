# Source code

This folder contains the code used to generate BPPSC instances from the original BPPS base instances.

## Included code

| File | Description |
|---|---|
| `generate_conflicts_rho_0_5_example.py` | Example conflict-generation script used for density `rho = 0.5` |

## Important note

The script `generate_conflicts_rho_0_5_example.py` is the version used for generating instances with conflict density `rho = 0.5`.

For other density levels, the same generation logic is used. Only the density parameter and the corresponding input/output folder paths should be changed.

The source codes of the MSIG algorithm and adapted benchmark algorithms are not included in this repository at this stage. This repository is intended to provide the generated benchmark instances, the conflict-generation procedure, and the computational results.
