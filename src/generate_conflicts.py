"""
Conflict generation script for BPPSC instances.

For each unordered pair of items (i,j), generate u_ij ~ U(0,1).
If u_ij <= rho, add conflict edge (i,j).
"""


def generate_conflict_edges(items, rho, seed=None):
    """Generate conflict edges for a given density rho."""
    pass


def extend_bpps_to_bppsc(base_instance, rho, seed=None):
    """Extend one BPPS instance into a BPPSC instance."""
    pass


def generate_all_densities(base_folder, output_folder):
    """Generate BPPSC instances for all density levels."""
    pass
