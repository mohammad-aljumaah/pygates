"""
pygates.gates

A collection of Boolean logic gate functions for educational, theoretical,
and practical use.

This module provides:

1. Core logic gates (commonly used in hardware and programming)
2. Derived logic functions (from Boolean algebra theory)

All functions:
- Accept any input type (converted to bool internally)
- Return a boolean value (True or False)

Author: Mohammad Aljumaah
https://mohammad-aljumaah.me

Last Updated: 2026-04-20
"""

from typing import Any


def _to_bool(value: Any) -> bool:
    """
    Convert any input value to a boolean.

    Parameters:
        value (Any): Input value

    Returns:
        bool: Boolean representation of the input
    """
    return bool(value)


# ========== Core logic gates ==========

def buffer_gate(a: Any) -> bool:
    """
    BUFFER gate.

    Returns the input value unchanged (after boolean conversion).

    Truth Table:
        A | OUT
        0 |  0
        1 |  1
    """
    return _to_bool(a)


def not_gate(a: Any) -> bool:
    """
    NOT gate (logical negation).

    Returns the inverse of the input.

    Truth Table:
        A | OUT
        0 |  1
        1 |  0
    """
    return not _to_bool(a)


def and_gate(a: Any, b: Any) -> bool:
    """
    AND gate.

    Returns True only if both inputs are True.

    Truth Table:
        A B | OUT
        0 0 |  0
        0 1 |  0
        1 0 |  0
        1 1 |  1
    """
    return _to_bool(a) and _to_bool(b)


def or_gate(a: Any, b: Any) -> bool:
    """
    OR gate.

    Returns True if at least one input is True.

    Truth Table:
        A B | OUT
        0 0 |  0
        0 1 |  1
        1 0 |  1
        1 1 |  1
    """
    return _to_bool(a) or _to_bool(b)


def xor_gate(a: Any, b: Any) -> bool:
    """
    XOR (exclusive OR) gate.

    Returns True if exactly one input is True.

    Truth Table:
        A B | OUT
        0 0 |  0
        0 1 |  1
        1 0 |  1
        1 1 |  0
    """
    a, b = _to_bool(a), _to_bool(b)
    return (a and not b) or (not a and b)


def nand_gate(a: Any, b: Any) -> bool:
    """
    NAND gate.

    Returns the negation of AND.

    Truth Table:
        A B | OUT
        0 0 |  1
        0 1 |  1
        1 0 |  1
        1 1 |  0
    """
    return not and_gate(a, b)


def nor_gate(a: Any, b: Any) -> bool:
    """
    NOR gate.

    Returns the negation of OR.

    Truth Table:
        A B | OUT
        0 0 |  1
        0 1 |  0
        1 0 |  0
        1 1 |  0
    """
    return not or_gate(a, b)


def xnor_gate(a: Any, b: Any) -> bool:
    """
    XNOR (equivalence) gate.

    Returns True if both inputs are the same.

    Truth Table:
        A B | OUT
        0 0 |  1
        0 1 |  0
        1 0 |  0
        1 1 |  1
    """
    return not xor_gate(a, b)


# ========== Derived / theoretical functions ==========

def implies(a: Any, b: Any) -> bool:
    """
    Logical implication (A → B).

    Returns False only when A is True and B is False.

    Truth Table:
        A B | OUT
        0 0 |  1
        0 1 |  1
        1 0 |  0
        1 1 |  1
    """
    a, b = _to_bool(a), _to_bool(b)
    return (not a) or b


def nimplies(a: Any, b: Any) -> bool:
    """
    Logical non-implication.

    Opposite of implication (A → B).

    Truth Table:
        A B | OUT
        0 0 |  0
        0 1 |  0
        1 0 |  1
        1 1 |  0
    """
    return not implies(a, b)


def a_gate(a: Any, b: Any) -> bool:
    """
    Identity gate (returns A).

    Ignores input B.

    Truth Table:
        A B | OUT
        0 x |  0
        1 x |  1
    """
    return _to_bool(a)


def b_gate(a: Any, b: Any) -> bool:
    """
    Identity gate (returns B).

    Ignores input A.

    Truth Table:
        A B | OUT
        x 0 |  0
        x 1 |  1
    """
    return _to_bool(b)


def not_a_gate(a: Any, b: Any) -> bool:
    """
    Negation of A.

    Ignores input B.

    Truth Table:
        A B | OUT
        0 x |  1
        1 x |  0
    """
    return not _to_bool(a)


def not_b_gate(a: Any, b: Any) -> bool:
    """
    Negation of B.

    Ignores input A.

    Truth Table:
        A B | OUT
        x 0 |  1
        x 1 |  0
    """
    return not _to_bool(b)


def true_gate(a: Any, b: Any) -> bool:
    """
    Constant TRUE function.

    Always returns True regardless of inputs.

    Truth Table:
        A B | OUT
        x x |  1
    """
    return True


def false_gate(a: Any, b: Any) -> bool:
    """
    Constant FALSE function.

    Always returns False regardless of inputs.

    Truth Table:
        A B | OUT
        x x |  0
    """
    return False
