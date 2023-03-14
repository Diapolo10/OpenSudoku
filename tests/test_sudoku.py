"""Tests the functionality of the sudoku object"""

# import pytest


def test_is_complete_unfinished(unfinished_sudoku):
    """Tests that the unfinished sudoku is not complete"""

    assert not unfinished_sudoku.is_complete(), unfinished_sudoku


def test_is_correct_unfinished(unfinished_sudoku):
    """Tests that the unfinished sudoku does not violate the rules"""

    assert unfinished_sudoku.is_correct(), unfinished_sudoku
