"""
pygates.examples

Simple examples for using pygates.
"""

from pygates import (
    and_gate,
    or_gate,
    not_gate,
    xor_gate,
    print_binary_truth_table,
    print_unary_truth_table,
)



# Basic usage

print("=== Basic Usage ===")

print("AND(1, 1):", and_gate(1, 1))
print("AND(1, 0):", and_gate(1, 0))

print("OR(0, 1):", or_gate(0, 1))

print("NOT(1):", not_gate(1))

print("XOR(1, 0):", xor_gate(1, 0))


# Truth tables

print("\n=== Truth Tables ===")

print_binary_truth_table("AND", and_gate)
print_unary_truth_table("NOT", not_gate)

