# Instance format

Each BPPSC instance contains the following information:

| Component | Description |
|---|---|
| `n` | Number of items |
| `m` | Number of setup classes |
| `d` | Bin capacity |
| `r` | Fixed bin-opening cost |
| `w_i` | Weight of item `i` |
| `c_i` | Class of item `i` |
| `s_c` | Setup capacity of class `c` |
| `f_c` | Setup cost of class `c` |
| `E` | Set of conflict edges |

## Feasibility

A feasible solution must satisfy:

1. each item is assigned to exactly one bin,
2. total item weight plus setup capacity does not exceed bin capacity,
3. no conflicting item pair is assigned to the same bin.
