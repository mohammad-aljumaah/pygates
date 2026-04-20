"""
Professional tests for pygates using pytest.
"""

import pytest
from pygates import *



@pytest.mark.parametrize("a,b,expected", [
    (0, 0, False),
    (0, 1, False),
    (1, 0, False),
    (1, 1, True),
])
def test_and(a, b, expected):
    assert and_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, False),
    (0, 1, True),
    (1, 0, True),
    (1, 1, True),
])
def test_or(a, b, expected):
    assert or_gate(a, b) is expected


@pytest.mark.parametrize("a,expected", [
    (0, True),
    (1, False),
])
def test_not(a, expected):
    assert not_gate(a) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, False),
    (0, 1, True),
    (1, 0, True),
    (1, 1, False),
])
def test_xor(a, b, expected):
    assert xor_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, True),
    (0, 1, True),
    (1, 0, True),
    (1, 1, False),
])
def test_nand(a, b, expected):
    assert nand_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, True),
    (0, 1, False),
    (1, 0, False),
    (1, 1, False),
])
def test_nor(a, b, expected):
    assert nor_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, True),
    (0, 1, False),
    (1, 0, False),
    (1, 1, True),
])
def test_xnor(a, b, expected):
    assert xnor_gate(a, b) is expected


@pytest.mark.parametrize("a,expected", [
    (0, False),
    (1, True),
])
def test_buffer(a, expected):
    assert buffer_gate(a) is expected


# =========================
# Derived functions
# =========================

@pytest.mark.parametrize("a,b,expected", [
    (0, 0, True),
    (0, 1, True),
    (1, 0, False),
    (1, 1, True),
])
def test_implies(a, b, expected):
    assert implies(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, False),
    (0, 1, False),
    (1, 0, True),
    (1, 1, False),
])
def test_nimplies(a, b, expected):
    assert nimplies(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, False),
    (0, 1, False),
    (1, 0, True),
    (1, 1, True),
])
def test_a_gate(a, b, expected):
    assert a_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, False),
    (0, 1, True),
    (1, 0, False),
    (1, 1, True),
])
def test_b_gate(a, b, expected):
    assert b_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, True),
    (1, 0, False),
])
def test_not_a_gate(a, b, expected):
    assert not_a_gate(a, b) is expected


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, True),
    (0, 1, False),
])
def test_not_b_gate(a, b, expected):
    assert not_b_gate(a, b) is expected


@pytest.mark.parametrize("a,b", [
    (0, 0),
    (1, 1),
])
def test_true_gate(a, b):
    assert true_gate(a, b) is True


@pytest.mark.parametrize("a,b", [
    (0, 0),
    (1, 1),
])
def test_false_gate(a, b):
    assert false_gate(a, b) is False

