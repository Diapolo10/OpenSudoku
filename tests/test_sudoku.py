"""Tests the functionality of the sudoku object"""

# import pytest

from open_sudoku.sudoku import Sudoku


def test_is_complete_unfinished(unfinished_sudoku: Sudoku):
    """Tests that the unfinished sudoku is not complete"""

    assert not unfinished_sudoku.is_complete(), f"\n{unfinished_sudoku}"


def test_is_correct_unfinished(unfinished_sudoku: Sudoku):
    """Tests that the unfinished sudoku does not violate the rules"""

    assert unfinished_sudoku.is_correct(), f"\n{unfinished_sudoku}"


def test_is_correct_unfinished_incorrect_row(unfinished_sudoku_incorrect_row: Sudoku):
    """Tests that incorrect rows violate the rules"""

    assert not unfinished_sudoku_incorrect_row.is_correct(), f"\n{unfinished_sudoku_incorrect_row}"


def test_is_correct_unfinished_incorrect_col(unfinished_sudoku_incorrect_col: Sudoku):
    """Tests that incorrect columns violate the rules"""

    assert not unfinished_sudoku_incorrect_col.is_correct(), f"\n{unfinished_sudoku_incorrect_col}"


def test_is_correct_unfinished_incorrect_grid(unfinished_sudoku_incorrect_grid: Sudoku):
    """Tests that incorrect squares violate the rules"""

    assert not unfinished_sudoku_incorrect_grid.is_correct(), f"\n{unfinished_sudoku_incorrect_grid}"


def test_is_complete_finished(finished_sudoku: Sudoku):
    """Tests that the finished sudoku is complete"""

    assert finished_sudoku.is_complete(), f"\n{finished_sudoku}"


def test_is_correct_finished(finished_sudoku: Sudoku):
    """Tests that the finished sudoku does not violate the rules"""

    assert finished_sudoku.is_correct(), f"\n{finished_sudoku}"


def test_is_correct_finished_incorrect(finished_incorrect_sudoku: Sudoku):
    """Tests that the incorrect sudoku violates the rules"""

    assert not finished_incorrect_sudoku.is_correct(), f"\n{finished_incorrect_sudoku}"
