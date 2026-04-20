"""
pygates.truth_tables

Utilities for generating and displaying truth tables for Boolean functions.

This module provides helper functions to visualize the behavior of
unary (1-input) and binary (2-input) logic functions.

All outputs are displayed in a clean, readable table format using 0/1 notation.

Author: Mohammad Aljumaah (mohammad-aljumaah.me)
Last Updated: 2026-04-20
"""

from typing import Callable


def print_unary_truth_table(name: str, func: Callable[[bool], bool]) -> None:
    """
    Print the truth table for a unary (single-input) Boolean function.

    Parameters:
        name (str): Name of the function (used for display)
        func (Callable[[bool], bool]): Function that takes one boolean input and returns a boolean output

    Output Format:
        Displays a table with input A and corresponding output.

        Example:
            Truth table for NOT
            A | OUT
            --|----
            0 |  1
            1 |  0

    Notes:
        - Inputs are evaluated as False (0) and True (1)
        - Output is converted to integer (0 or 1) for readability
    """

    print(f"Truth table for {name}")
    print("A | OUT")
    print("--|----")

    for a in (False, True):
        print(f"{int(a)} |  {int(func(a))}")


def print_binary_truth_table(name: str, func: Callable[[bool, bool], bool]) -> None:
    """
    Print the truth table for a binary (two-input) Boolean function.

    Parameters:
        name (str): Name of the function (used for display)
        func (Callable[[bool, bool], bool]): Function that takes two boolean inputs and returns a boolean output

    Output Format:
        Displays a table with inputs A, B and corresponding output.

        Example:
            Truth table for AND
            A B | OUT
            ----|----
            0 0 |  0
            0 1 |  0
            1 0 |  0
            1 1 |  1

    Notes:
        - Inputs are evaluated as False (0) and True (1)
        - Output is converted to integer (0 or 1) for readability
        - All possible input combinations are evaluated
    """

    print(f"Truth table for {name}")
    print("A B | OUT")
    print("----|----")

    for a in (False, True):
        for b in (False, True):
            print(f"{int(a)} {int(b)} |  {int(func(a, b))}")
