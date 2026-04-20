from .gates import (
    buffer_gate,
    not_gate,
    and_gate,
    or_gate,
    xor_gate,
    nand_gate,
    nor_gate,
    xnor_gate,
    implies,
    nimplies,
    a_gate,
    b_gate,
    not_a_gate,
    not_b_gate,
    true_gate,
    false_gate,
)

from .truth_tables import (
    print_unary_truth_table,
    print_binary_truth_table,
)

__version__ = "0.1.0"