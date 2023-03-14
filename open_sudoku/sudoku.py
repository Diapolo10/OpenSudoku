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

        # Validate rows
        for row in self.board:
            if len(set(row)) != self.width and EMPTY_SLOT not in row:
                return False

        # Validate cols
        for col in zip(*self.board):
            if any(col.count(num) != 1 for num in range(1, self.width+1)) and EMPTY_SLOT not in col:
                return False

        # Validate grids
        for cols in into_groups(self.board, self.subgrid_height):
            grids = list(join_adjacent_groups(list(zip(*cols)), self.subgrid_width))

            for grid in grids:
                if len(set(grid)) != self.width and EMPTY_SLOT not in grid:
                    return False

        return True

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

    def insert_number(self, number: int, x_coord: int, y_coord: int):
        """Attempts to insert a number into the grid"""

        if (x_coord, y_coord) in self.fixed_numbers:
            raise ValueError("Slot cannot be changed")

        previous = self.board[y_coord][x_coord]
        self.board[y_coord][x_coord] = number

        if self.strict and not self.is_correct():
            self.board[y_coord][x_coord] = previous
            raise ValueError("Number is invalid for this slot")
