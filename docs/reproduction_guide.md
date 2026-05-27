# Reproduction guide

This document explains how to reproduce the computational results.

## Step 1: Install packages

```bash
pip install -r requirements.txt
python scripts/run_single_instance.py --instance data/toy_example/toy_bppsc_instance.txt --algorithm msig
python scripts/run_all_by_density.py --rho 0.4
python scripts/reproduce_tables.py
results/

Commit:

```bash
git add docs/
git commit -m "Add documentation files"
git push
lws
cat > figures/README.md <<'EOF'
# Figures

This folder contains figures summarizing the computational results.

Suggested figures:

| Figure | Description |
|---|---|
| `gap_by_density.png` | Average deviation by conflict density |
| `best_count_by_density.png` | Number of best solutions by density |
| `deviation_by_problem_size.png` | Average deviation by problem size |
| `cpu_time_by_n.png` | Average CPU time by number of items |
