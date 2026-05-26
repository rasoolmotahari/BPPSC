# BPPSC instances for rho = 0.8

This folder contains 480 BPPSC instances generated with conflict density `rho = 0.8`.

Each instance is generated from a BPPS base instance by adding pairwise conflicts between items.

A conflict edge `(i,j)` is generated if:

```text
u_ij <= 0.8
```

where `u_ij` is sampled from `U(0,1)`.
