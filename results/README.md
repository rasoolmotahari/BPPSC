# Results

This folder contains the computational results of the BPPSC experiments.

## Structure

| Folder | Description |
|---|---|
| `by_density/` | Results separated by conflict density |
| `by_problem_size/` | Results separated by number of items |
| `tables_for_paper/` | Tables reported in the paper |

## Algorithms

The following algorithms are compared:

- P-FFD
- P-BFD
- P-WFD
- Best C-TP
- MSIG

## Performance measure

For each instance, the deviation of algorithm `a` is computed as:

```text
Dev_a (%) = ((z_a - z_best) / z_best) * 100
```

where `z_best` is the best solution found among all compared algorithms for that instance.
