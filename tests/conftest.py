"""Contains global fixtures for unit tests"""

import pytest

from open_sudoku.sudoku import Sudoku


@pytest.fixture(scope='session')
def unfinished_correct_board():
    test_board_layout = [
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

    return test_board_layout


@pytest.fixture(scope='session')
def unfinished_correct_board_small():
    test_board_layout = [
        [0, 0, 3, 0, 1, 0],
        [2, 0, 0, 1, 6, 3],
        [0, 5, 0, 0, 2, 0],
        [1, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 5, 2, 0, 6],
    ]

    return test_board_layout


@pytest.fixture(scope='function')
def unfinished_sudoku(unfinished_correct_board):

    return Sudoku(board=unfinished_correct_board)


@pytest.fixture(scope='function')
def unfinished_sudoku_small(unfinished_correct_board_small):

    return Sudoku(board=unfinished_correct_board_small, subgrid_width=3, subgrid_height=2)


@pytest.fixture(scope='function')
def strict_unfinished_sudoku(unfinished_correct_board):

    return Sudoku(board=unfinished_correct_board, strict=True)


@pytest.fixture(scope='function')
def strict_unfinished_sudoku_small(unfinished_correct_board_small):

    return Sudoku(board=unfinished_correct_board_small, subgrid_width=3, subgrid_height=2, strict=True)
