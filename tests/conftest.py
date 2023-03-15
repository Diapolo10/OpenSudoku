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
        [0, 3, 0, 0, 4, 0],
        [1, 4, 6, 0, 3, 2],
        [0, 1, 5, 2, 6, 0],
        [2, 6, 0, 0, 0, 0],
        [4, 2, 0, 0, 1, 5],
        [0, 5, 0, 4, 0, 0],
    ]

    return test_board_layout


@pytest.fixture(scope='session')
def finished_correct_board():
    test_board_layout = [
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

    return test_board_layout


@pytest.fixture(scope='session')
def finished_correct_board_small():
    test_board_layout = [
        [5, 3, 2, 1, 4, 6],
        [1, 4, 6, 5, 3, 1],
        [3, 1, 5, 2, 6, 4],
        [2, 6, 4, 3, 5, 1],
        [4, 2, 3, 6, 1, 5],
        [6, 5, 1, 4, 2, 3],
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
