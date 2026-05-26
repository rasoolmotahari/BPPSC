# Data

This folder contains the benchmark data used in the computational study.

## Structure

| Folder | Description |
|---|---|
| `toy_example/` | A small example instance for testing the code |
| `bpps_base_instances/` | Original BPPS base instances used as the starting point |
| `bppsc_instances/` | Generated BPPSC instances with conflict densities from 0.0 to 0.9 |

## Conflict generation

For each unordered item pair `(i,j)`, a random number `u_ij` is generated from `U(0,1)`.

A conflict edge is added if:

```text
u_ij <= rho
```

where `rho` is the conflict-density parameter.

## Density levels

The following density levels are included:

```text
rho = 0.0, 0.1, 0.2, ..., 0.9
```

Each density folder contains 480 instances.
