# Data

This folder contains the benchmark data used in the computational study.

## Structure

| Folder                 | Description |
| ---------------------- | ----------- |
| `bpps_base_instances/` | Original BPPS base instances used as the starting point |
| `bppsc_instances/`     | Generated BPPSC instances with conflict densities from 0.0 to 0.9 |

## Conflict generation

For each unordered item pair `(i,j)`, a random number `u_ij` is generated from `U(0,1)`.

A conflict edge is added if:

```text
u_ij <= rho
