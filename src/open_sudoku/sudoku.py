"""A simple Sudoku game implementation."""

from __future__ import annotations

from functools import cache
from typing import TYPE_CHECKING

from open_sudoku.config import EMPTY_SLOT, InsertionMode
from open_sudoku.custom_itertools import into_groups, join_adjacent_groups
from open_sudoku.debug_rendering import generate_board

if TYPE_CHECKING:
    from collections.abc import Iterable

    from open_sudoku.config import SudokuBoard, T


class Sudoku:
    """A game of Sudoku."""

    def __init__(self,
                 board: SudokuBoard,
                 subgrid_width: int = 3,
                 subgrid_height: int = 3,
                 insertion_mode: InsertionMode = InsertionMode.RELAXED) -> None:
        """Initialise a sudoku board."""
        self.board = board
        self.fixed_numbers = self._fixed_numbers(tuple(tuple(row) for row in self.board))
        self.width = len(board[0])
        self.height = len(board)
        self.subgrid_width = subgrid_width
        self.subgrid_height = subgrid_height
        self.insertion_mode = insertion_mode

    def __str__(self) -> str:
        """Pretty-print the current board."""
        return generate_board(self.board, self.subgrid_width, self.subgrid_height)

    def __repr__(self) -> str:
        """Debug representation."""
        return (
            f"{type(self)}(width={self.width}, height={self.height},"
            f" subgrid_width={self.subgrid_width}, subgrid_height={self.subgrid_height})"
        )

    def is_complete(self) -> bool:
        """Check if the board is filled out."""
        for row in self.board:
            if row.count(EMPTY_SLOT):
                return False

        return self.is_correct()

    def is_correct(self) -> bool:
        """Validate the current board state."""
        return (
            self.validate_rows()
            and self.validate_cols()
            and self.validate_grids()
        )

    def validate_rows(self) -> bool:
        """Validate the rows of the board."""
        rows = self.board
        return self._is_unique(rows, ignored_value=EMPTY_SLOT)

    def validate_cols(self) -> bool:
        """Validate the columns of the board."""
        cols = zip(*self.board, strict=False)
        return self._is_unique(cols, ignored_value=EMPTY_SLOT)

    def validate_grids(self) -> bool:
        """Validate the grids of the board."""
        return all(
            self._is_unique(grids, ignored_value=EMPTY_SLOT)
            for cols in into_groups(self.board, self.subgrid_height)
            if (grids := join_adjacent_groups(list(zip(*cols, strict=False)), self.subgrid_width))
        )

    @staticmethod
    @cache
    def _fixed_numbers(board: SudokuBoard) -> list[tuple[int, int]]:
        """Find the initial known numbers."""
        return [
            (x, y)
            for y, row in enumerate(board)
            for x, cell in enumerate(row)
            if cell != EMPTY_SLOT
        ]

    @staticmethod
    @cache
    def _possible_values(board: SudokuBoard,
                         fixed_values: list[tuple[int, int]],
                         max_num: int) -> list[list[list[int] | None]]:
        """Find the possible values for every empty square on the board."""
        result = [
            [
                list(range(1, max_num+1)) if (x, y) not in fixed_values else None
                for x, _ in enumerate(row)
            ]
            for y, row in enumerate(board)
        ]

        for _idx, (_board_row, _values_row) in enumerate(zip(board, result, strict=False)):
            pass

        return result

    @staticmethod
    def _is_unique(iterable: Iterable[Iterable[T]], ignored_value: T) -> bool:
        """Check a 2D iterable for uniqueness."""
        for inner_iter in iterable:
            filtered_inner_iter = [
                value
                for value in inner_iter
                if value != ignored_value
            ]
            if len(set(filtered_inner_iter)) != len(filtered_inner_iter):
                return False
        return True

    def insert_number(self, number: int, x_coord: int, y_coord: int) -> None:
        """Attempt to insert a number into the grid."""
        if (x_coord, y_coord) in self.fixed_numbers:
            msg = "Slot cannot be changed"
            raise ValueError(msg)

        previous = self.board[y_coord][x_coord]
        self.board[y_coord][x_coord] = number

        if self.insertion_mode == InsertionMode.STRICT and not self.is_correct():
            self.board[y_coord][x_coord] = previous
            msg = "Number is invalid for this slot"
            raise ValueError(msg)
