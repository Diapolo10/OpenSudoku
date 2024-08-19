"""Contains global fixtures for unit tests."""

import pytest

from open_sudoku.sudoku import Sudoku, SudokuBoard


@pytest.fixture(scope='session')
def unfinished_correct_board() -> SudokuBoard:
    """Return an unfinished but correct board layout."""
    return [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]


@pytest.fixture(scope='session')
def unfinished_correct_board_small() -> SudokuBoard:
    """Return an unfinished but correct, small board layout."""
    return [
        [0, 3, 0, 0, 4, 0],
        [1, 4, 6, 0, 3, 2],
        [0, 1, 5, 2, 6, 0],
        [2, 6, 0, 0, 0, 0],
        [4, 2, 0, 0, 1, 5],
        [0, 5, 0, 4, 0, 0],
    ]


@pytest.fixture(scope='session')
def finished_correct_board() -> SudokuBoard:
    """Return a filled and correct board layout."""
    return [
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9],
    ]


@pytest.fixture(scope='session')
def finished_correct_board_small() -> SudokuBoard:
    """Return a filled and correct, small board layout."""
    return [
        [5, 3, 2, 1, 4, 6],
        [1, 4, 6, 5, 3, 2],
        [3, 1, 5, 2, 6, 4],
        [2, 6, 4, 3, 5, 1],
        [4, 2, 3, 6, 1, 5],
        [6, 5, 1, 4, 2, 3],
    ]


@pytest.fixture(scope='session')
def unfinished_board_incorrect_row() -> SudokuBoard:
    """Return an unfinished board layout with an incorrect row."""
    return [
        [3, 0, 6, 5, 3, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]


@pytest.fixture(scope='session')
def unfinished_board_incorrect_col() -> SudokuBoard:
    """Return an unfinished board layout with an incorrect column."""
    return [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [9, 0, 5, 2, 0, 6, 3, 0, 0],
    ]


@pytest.fixture(scope='session')
def unfinished_board_incorrect_grid() -> SudokuBoard:
    """Return an unfinished board layout with an incorrect grid."""
    return [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 8, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]


@pytest.fixture(scope='session')
def unfinished_incorrect_board_small() -> SudokuBoard:
    """Return an unfinished, incorrect, small board layout."""
    return [
        [0, 3, 0, 0, 4, 0],
        [1, 4, 6, 0, 3, 2],
        [0, 1, 5, 2, 6, 0],
        [2, 6, 0, 0, 0, 0],
        [4, 2, 1, 0, 1, 5],
        [0, 5, 0, 4, 0, 0],
    ]


@pytest.fixture(scope='session')
def finished_incorrect_board() -> SudokuBoard:
    """Return a filled but incorrect board layout."""
    return [
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 5, 6, 8],
        [4, 8, 7, 6, 2, 9, 7, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9],
    ]


@pytest.fixture(scope='session')
def finished_incorrect_board_small() -> SudokuBoard:
    """Return a filled but incorrect, small board layout."""
    return [
        [5, 3, 2, 1, 4, 6],
        [1, 4, 6, 5, 3, 1],
        [3, 1, 5, 2, 6, 4],
        [2, 6, 3, 4, 5, 1],
        [4, 2, 3, 6, 1, 5],
        [6, 5, 1, 4, 2, 3],
    ]


@pytest.fixture
def unfinished_sudoku(unfinished_correct_board: SudokuBoard) -> Sudoku:
    """Return an unfinished but correct sudoku instance."""
    return Sudoku(board=unfinished_correct_board)


@pytest.fixture
def unfinished_sudoku_small(unfinished_correct_board_small: SudokuBoard) -> Sudoku:
    """Return an unfinished but correct, small sudoku instance."""
    return Sudoku(board=unfinished_correct_board_small, subgrid_width=3, subgrid_height=2)


@pytest.fixture
def finished_sudoku(finished_correct_board: SudokuBoard) -> Sudoku:
    """Return a finished and correct sudoku instance."""
    return Sudoku(board=finished_correct_board)


@pytest.fixture
def finished_sudoku_small(finished_correct_board_small: SudokuBoard) -> Sudoku:
    """Return a finished and correct, small sudoku instance."""
    return Sudoku(board=finished_correct_board_small, subgrid_width=3, subgrid_height=2)


@pytest.fixture
def unfinished_sudoku_incorrect_row(unfinished_board_incorrect_row: SudokuBoard) -> Sudoku:
    """Return an unfinished sudoku instance with an incorrect row."""
    return Sudoku(board=unfinished_board_incorrect_row)


@pytest.fixture
def unfinished_sudoku_incorrect_col(unfinished_board_incorrect_col: SudokuBoard) -> Sudoku:
    """Return an unfinished sudoku instance with an incorrect column."""
    return Sudoku(board=unfinished_board_incorrect_col)


@pytest.fixture
def unfinished_sudoku_incorrect_grid(unfinished_board_incorrect_grid: SudokuBoard) -> Sudoku:
    """Return an unfinished sudoku instance with an incorrect grid."""
    return Sudoku(board=unfinished_board_incorrect_grid)


@pytest.fixture
def unfinished_incorrect_sudoku_small(unfinished_incorrect_board_small: SudokuBoard) -> Sudoku:
    """Return an unfinished, incorrect, small sudoku instance."""
    return Sudoku(board=unfinished_incorrect_board_small, subgrid_width=3, subgrid_height=2)


@pytest.fixture
def finished_incorrect_sudoku(finished_incorrect_board: SudokuBoard) -> Sudoku:
    """Return a finished but incorrect sudoku instance."""
    return Sudoku(board=finished_incorrect_board)


@pytest.fixture
def finished_incorrect_sudoku_small(finished_incorrect_board_small: SudokuBoard) -> Sudoku:
    """Return a finished but incorrect, small sudoku instance."""
    return Sudoku(board=finished_incorrect_board_small, subgrid_width=3, subgrid_height=2)
