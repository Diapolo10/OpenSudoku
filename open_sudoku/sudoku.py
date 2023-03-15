"""A simple Sudoku game implementation"""

from collections.abc import Iterable, Iterator, MutableSequence, Sequence
from functools import cache
from typing import TypeVar

SudokuBoard = Sequence[MutableSequence[int]]
T = TypeVar('T')
U = TypeVar('U')

EMPTY_SLOT = 0


def into_groups(iterable: Iterable[T], group_size: int = 1) -> Iterator[tuple[T, ...]]:
    """Groups a 1D iterable into an iterable of tuples of a given size"""

    return zip(*(iter(iterable),) * group_size)


def join_adjacent_groups(sequence: Sequence[T], group_size: int = 1) -> Iterator[tuple[T]]:
    """Joins groups of n adjacent values to one"""

    return (
        sum(sub, start=type(sequence[0])())  # type: ignore[call-overload]
        for sub in zip(
            *(
                sequence[n::group_size]
                for n in range(group_size)
            )
        )
    )


class Sudoku:
    """Implements a game of Sudoku"""

    def __init__(self, board: SudokuBoard, subgrid_width: int = 3, subgrid_height: int = 3, strict: bool = False):
        self.board = board
        self.fixed_numbers = self._fixed_numbers(tuple(tuple(row) for row in self.board))
        self.width = len(board[0])
        self.height = len(board)
        self.subgrid_width = subgrid_width
        self.subgrid_height = subgrid_height
        self.strict = strict

    def __str__(self) -> str:
        """Pretty-prints the current board"""

        # NOTE: Switch from hard-coded to calculated,
        #       and cache until board is replaced (via property)
        top_border = "\n╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n"
        mid_border = "\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
        big_border = "\n╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n"
        bot_border = "\n╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n"
        rows = []

        for idx, row in enumerate(self.board):
            formatted_row = '║ ' + ' ║ '.join(
                ' │ '.join(
                    map(
                        lambda x: str(x) if x != EMPTY_SLOT else ' ',
                        cell_row
                    )
                )
                for cell_row in into_groups(row, self.subgrid_width)
            ) + ' ║'

            if idx != 0 and idx % self.subgrid_height == 0:
                rows.append(big_border)

            elif idx not in (0,  self.height):
                rows.append(mid_border)

            rows.append(formatted_row)

        return f"{top_border}{''.join(rows)}{bot_border}".strip()

    def is_complete(self) -> bool:
        """Checks if the board is filled out"""

        for row in self.board:
            if row.count(EMPTY_SLOT):
                return False

        return self.is_correct()

    def is_correct(self) -> bool:
        """Validates the current board state"""

        return (
            self.validate_rows()
            and self.validate_cols()
            and self.validate_grids()
        )

    def validate_rows(self):
        """Validates the rows of the board"""

        rows = self.board
        return self._is_unique(rows, ignored_value=EMPTY_SLOT)

    def validate_cols(self):
        """Validates the columns of the board"""

        cols = zip(*self.board)
        return self._is_unique(cols, ignored_value=EMPTY_SLOT)

    def validate_grids(self):
        """Validates the grids of the board"""

        return all(
            self._is_unique(grids, ignored_value=EMPTY_SLOT)
            for cols in into_groups(self.board, self.subgrid_height)
            if (grids := join_adjacent_groups(list(zip(*cols)), self.subgrid_width))
        )

    @staticmethod
    @cache
    def _fixed_numbers(board: SudokuBoard) -> list[tuple[int, int]]:
        """Finds the initial known numbers"""

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
        """Finds the possible values for every empty square on the board"""

        result = [
            [
                list(range(1, max_num+1)) if (x, y) not in fixed_values else None
                for x, _ in enumerate(row)
            ]
            for y, row in enumerate(board)
        ]

        return result

    @staticmethod
    def _is_unique(iterable: Iterable[Iterable[T]], ignored_value: T) -> bool:
        """Checks a 2D iterable for uniqueness"""

        for inner_iter in iterable:
            filtered_inner_iter = [
                value
                for value in inner_iter
                if value != ignored_value
            ]
            if len(set(filtered_inner_iter)) != len(filtered_inner_iter):
                return False
        return True

    def insert_number(self, number: int, x_coord: int, y_coord: int):
        """Attempts to insert a number into the grid"""

        if (x_coord, y_coord) in self.fixed_numbers:
            raise ValueError("Slot cannot be changed")

        previous = self.board[y_coord][x_coord]
        self.board[y_coord][x_coord] = number

        if self.strict and not self.is_correct():
            self.board[y_coord][x_coord] = previous
            raise ValueError("Number is invalid for this slot")
