"""
Tests for pygates.gates
Covers all 16 Boolean functions.
"""

from pygates import *


# =========================
# Core gates
# =========================

def test_and():
    assert and_gate(0, 0) is False
    assert and_gate(0, 1) is False
    assert and_gate(1, 0) is False
    assert and_gate(1, 1) is True


def test_or():
    assert or_gate(0, 0) is False
    assert or_gate(0, 1) is True
    assert or_gate(1, 0) is True
    assert or_gate(1, 1) is True


def test_not():
    assert not_gate(0) is True
    assert not_gate(1) is False


def test_xor():
    assert xor_gate(0, 0) is False
    assert xor_gate(0, 1) is True
    assert xor_gate(1, 0) is True
    assert xor_gate(1, 1) is False


def test_nand():
    assert nand_gate(0, 0) is True
    assert nand_gate(0, 1) is True
    assert nand_gate(1, 0) is True
    assert nand_gate(1, 1) is False


def test_nor():
    assert nor_gate(0, 0) is True
    assert nor_gate(0, 1) is False
    assert nor_gate(1, 0) is False
    assert nor_gate(1, 1) is False


def test_xnor():
    assert xnor_gate(0, 0) is True
    assert xnor_gate(0, 1) is False
    assert xnor_gate(1, 0) is False
    assert xnor_gate(1, 1) is True


def test_buffer():
    assert buffer_gate(0) is False
    assert buffer_gate(1) is True


# =========================
# Derived / theory functions
# =========================

def test_implies():
    assert implies(0, 0) is True
    assert implies(0, 1) is True
    assert implies(1, 0) is False
    assert implies(1, 1) is True


def test_nimplies():
    assert nimplies(0, 0) is False
    assert nimplies(0, 1) is False
    assert nimplies(1, 0) is True
    assert nimplies(1, 1) is False


def test_a_gate():
    assert a_gate(0, 0) is False
    assert a_gate(0, 1) is False
    assert a_gate(1, 0) is True
    assert a_gate(1, 1) is True


def test_b_gate():
    assert b_gate(0, 0) is False
    assert b_gate(0, 1) is True
    assert b_gate(1, 0) is False
    assert b_gate(1, 1) is True


def test_not_a_gate():
    assert not_a_gate(0, 0) is True
    assert not_a_gate(1, 0) is False


def test_not_b_gate():
    assert not_b_gate(0, 0) is True
    assert not_b_gate(0, 1) is False


def test_true_gate():
    assert true_gate(0, 0) is True
    assert true_gate(1, 1) is True


def test_false_gate():
    assert false_gate(0, 0) is False
    assert false_gate(1, 1) is False


# =========================
# Runner 

def run_tests():
    print("Running all tests...")

    test_and()
    test_or()
    test_not()
    test_xor()
    test_nand()
    test_nor()
    test_xnor()
    test_buffer()

    test_implies()
    test_nimplies()
    test_a_gate()
    test_b_gate()
    test_not_a_gate()
    test_not_b_gate()
    test_true_gate()
    test_false_gate()

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()