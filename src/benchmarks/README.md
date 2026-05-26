# Benchmark algorithms

This folder contains adapted benchmark algorithms for BPPSC.

## Algorithms

| File | Algorithm |
|---|---|
| `p_ffd.py` | Parametric First-Fit Decreasing |
| `p_bfd.py` | Parametric Best-Fit Decreasing |
| `p_wfd.py` | Parametric Worst-Fit Decreasing |
| `c_tp_ffd.py` | Conflict-aware two-phase BPPS method using FFD |
| `c_tp_bfd.py` | Conflict-aware two-phase BPPS method using BFD |

The final C-TP result is the best solution obtained from `c_tp_ffd.py` and `c_tp_bfd.py`.
