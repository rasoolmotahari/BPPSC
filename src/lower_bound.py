"""
Lower-bound procedures for BPPSC.

Includes:
1. setup-capacity lower bound,
2. clique-based improved lower bound,
3. optional assignment-based lower-bound model.
"""


def compute_gamma_values(instance):
    """Compute the minimum number of setup activations for each class."""
    pass


def compute_beta_value(instance, gamma):
    """Compute the lower bound on the number of bins."""
    pass


def find_global_clique(instance):
    """Find a global maximal clique in the conflict graph."""
    pass


def find_class_cliques(instance):
    """Find class-specific maximal cliques."""
    pass


def compute_improved_lower_bound(instance):
    """Compute the improved BPPSC lower bound."""
    pass


def solve_assignment_based_lb(instance):
    """Solve the optional assignment-based lower-bound model."""
    pass
