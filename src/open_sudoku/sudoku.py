"""A simple Sudoku game implementation."""

from __future__ import annotations

from collections.abc import Iterable, Iterator, MutableSequence, Sequence
from enum import IntEnum, auto
from functools import cache
from typing import TypedDict, TypeVar

SudokuBoard = Sequence[MutableSequence[int]]
T = TypeVar('T')
U = TypeVar('U')

EMPTY_SLOT = 0


class InsertionMode(IntEnum):
    """Rules for inserting numbers."""

    RELAXED = auto()
    STRICT = auto()


class BoardBorderCharacterMap(TypedDict):
    """Map board border components to characters."""

    left_side: str
    right_side: str
    horizontal_line: str
    subgrid_separator: str
    cell_separator: str


class BoardNumberCharacterMap(TypedDict):
    """Map board number components to characters."""

    border: str
    cell_border: str


TOP_BORDER_CHARS: BoardBorderCharacterMap = {
    'left_side': '╔',
    'right_side': '╗',
    'horizontal_line': '═',
    'subgrid_separator': '╦',
    'cell_separator': '╤',
}
BOTTOM_BORDER_CHARS: BoardBorderCharacterMap = {
    'left_side': '╚',
    'right_side': '╝',
    'horizontal_line': '═',
    'subgrid_separator': '╩',
    'cell_separator': '╧',
}
MID_BORDER_CHARS: BoardBorderCharacterMap = {
    'left_side': '╟',
    'right_side': '╢',
    'horizontal_line': '─',
    'subgrid_separator': '╫',
    'cell_separator': '┼',
}
BIG_BORDER_CHARS: BoardBorderCharacterMap = {
    'left_side': '╠',
    'right_side': '╣',
    'horizontal_line': '═',
    'subgrid_separator': '╬',
    'cell_separator': '╪',
}
NUM_BORDER_CHARS: BoardNumberCharacterMap = {
    'border': '║',
    'cell_border': '│',
}


def into_groups(iterable: Iterable[T], group_size: int = 1) -> Iterator[tuple[T, ...]]:
    """Group a 1D iterable into an iterable of tuples of a given size."""
    return zip(*(iter(iterable),) * group_size, strict=False)


def join_adjacent_groups(sequence: Sequence[T], group_size: int = 1) -> Iterator[tuple[T]]:
    """Join groups of n adjacent values to one."""
    return (
        sum(sub, start=type(sequence[0])())  # type: ignore[call-overload]
        for sub in zip(
            *(
                sequence[n::group_size]
                for n in range(group_size)
            ), strict=False,
        )
    )


def generate_row(board_cols: int, board_subgrid_cols: int, chars: BoardBorderCharacterMap) -> str:
    """Generate row for the sudoku board text representation."""
    return (
        chars['left_side']
        + chars['subgrid_separator'].join(
            chars['cell_separator'].join(
                chars['horizontal_line'] * 3
                for _ in range(board_subgrid_cols)
            )
            for _ in range(board_cols // board_subgrid_cols)
        )
        + chars['right_side']
    )


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
        # NOTE: Cache until board is replaced (via property)
        top_border = f"\n{generate_row(self.width, self.subgrid_width, TOP_BORDER_CHARS)}\n"
        mid_border = f"\n{generate_row(self.width, self.subgrid_width, MID_BORDER_CHARS)}\n"
        big_border = f"\n{generate_row(self.width, self.subgrid_width, BIG_BORDER_CHARS)}\n"
        bot_border = f"\n{generate_row(self.width, self.subgrid_width, BOTTOM_BORDER_CHARS)}\n"
        rows = []

        for idx, row in enumerate(self.board):
            formatted_row = f'{NUM_BORDER_CHARS["border"]} ' + f' {NUM_BORDER_CHARS["border"]} '.join(
                f' {NUM_BORDER_CHARS["cell_border"]} '.join(
                    (str(x) if x != EMPTY_SLOT else ' ' for x in cell_row),
                )
                for cell_row in into_groups(row, self.subgrid_width)
            ) + f' {NUM_BORDER_CHARS["border"]}'

            if idx != 0 and idx % self.subgrid_height == 0:
                rows.append(big_border)

            elif idx not in (0,  self.height):
                rows.append(mid_border)

            rows.append(formatted_row)

        return f"{top_border}{''.join(rows)}{bot_border}".strip()

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
