"""Tests the functionality of the sudoku object."""

from open_sudoku.sudoku import Sudoku


def test_is_complete_unfinished(unfinished_sudoku: Sudoku):
    """Test that the unfinished sudoku is not complete."""
    assert not unfinished_sudoku.is_complete(), f"\n{unfinished_sudoku}"


def test_is_correct_unfinished(unfinished_sudoku: Sudoku):
    """Test that the unfinished sudoku does not violate the rules."""
    assert unfinished_sudoku.is_correct(), f"\n{unfinished_sudoku}"


def test_is_correct_unfinished_incorrect_row(unfinished_sudoku_incorrect_row: Sudoku):
    """Test that incorrect rows violate the rules."""
    assert not unfinished_sudoku_incorrect_row.is_correct(), f"\n{unfinished_sudoku_incorrect_row}"


def test_is_correct_unfinished_incorrect_col(unfinished_sudoku_incorrect_col: Sudoku):
    """Test that incorrect columns violate the rules."""
    assert not unfinished_sudoku_incorrect_col.is_correct(), f"\n{unfinished_sudoku_incorrect_col}"


def test_is_correct_unfinished_incorrect_grid(unfinished_sudoku_incorrect_grid: Sudoku):
    """Test that incorrect squares violate the rules."""
    assert not unfinished_sudoku_incorrect_grid.is_correct(), f"\n{unfinished_sudoku_incorrect_grid}"


def test_is_complete_finished(finished_sudoku: Sudoku):
    """Test that the finished sudoku is complete."""
    assert finished_sudoku.is_complete(), f"\n{finished_sudoku}"


def test_is_correct_finished(finished_sudoku: Sudoku):
    """Test that the finished sudoku does not violate the rules."""
    assert finished_sudoku.is_correct(), f"\n{finished_sudoku}"


def test_is_correct_finished_incorrect(finished_incorrect_sudoku: Sudoku):
    """Test that the incorrect small sudoku violates the rules."""
    assert not finished_incorrect_sudoku.is_correct(), f"\n{finished_incorrect_sudoku}"


def test_is_complete_unfinished_small(unfinished_sudoku_small: Sudoku):
    """Test that the unfinished small sudoku is not complete."""
    assert not unfinished_sudoku_small.is_complete(), f"\n{unfinished_sudoku_small}"


def test_is_correct_unfinished_small(unfinished_sudoku_small: Sudoku):
    """Test that the unfinished small sudoku does not violate the rules."""
    assert unfinished_sudoku_small.is_correct(), f"\n{unfinished_sudoku_small}"


def test_is_complete_finished_small(finished_sudoku_small: Sudoku):
    """Test that the finished small sudoku is complete."""
    assert finished_sudoku_small.is_complete(), f"\n{finished_sudoku_small}"


def test_is_correct_finished_small(finished_sudoku_small: Sudoku):
    """Test that the finished small sudoku does not violate the rules."""
    assert finished_sudoku_small.is_correct(), f"\n{finished_sudoku_small}"


def test_is_correct_finished_incorrect_small(finished_incorrect_sudoku_small: Sudoku):
    """Test that the incorrect small sudoku violates the rules."""
    assert not finished_incorrect_sudoku_small.is_correct(), f"\n{finished_incorrect_sudoku_small}"
