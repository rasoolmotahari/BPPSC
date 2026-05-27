# Result format

Each result file contains one row per instance and algorithm.

## Columns

| Column | Description |
|---|---|
| `instance_name` | Instance identifier |
| `rho` | Conflict density |
| `n` | Number of items |
| `algorithm` | Algorithm name |
| `objective` | Objective value |
| `lower_bound` | Lower-bound value |
| `gap_lb` | Gap to lower bound |
| `time` | CPU time in seconds |
| `best_found` | Best objective found among all algorithms |
| `deviation` | Deviation from best found solution |
| `is_best` | 1 if the algorithm obtains the best or tied-best solution |
