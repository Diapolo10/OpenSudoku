"""Helper functions for printing debug messages."""

from __future__ import annotations

from functools import cache
from typing import TypedDict

from open_sudoku.config import EMPTY_SLOT, SudokuBoard
from open_sudoku.custom_itertools import into_groups


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


def generate_board(board: SudokuBoard, subgrid_rows: int, subgrid_cols: int) -> str:
    """Render a text representation of a Sudoku board."""
    return _generate_board(tuple(tuple(row) for row in board), subgrid_rows, subgrid_cols)

@cache
def _generate_board(board: tuple[tuple[int, ...], ...], subgrid_rows: int, subgrid_cols: int) -> str:
    width = len(board[0])
    height = len(board)
    top_border = f"\n{generate_row(width, subgrid_cols, TOP_BORDER_CHARS)}\n"
    mid_border = f"\n{generate_row(width, subgrid_cols, MID_BORDER_CHARS)}\n"
    big_border = f"\n{generate_row(width, subgrid_cols, BIG_BORDER_CHARS)}\n"
    bot_border = f"\n{generate_row(width, subgrid_cols, BOTTOM_BORDER_CHARS)}\n"
    rows = []

    for idx, row in enumerate(board):
        formatted_row = f'{NUM_BORDER_CHARS["border"]} ' + f' {NUM_BORDER_CHARS["border"]} '.join(
            f' {NUM_BORDER_CHARS["cell_border"]} '.join(
                (str(x) if x != EMPTY_SLOT else ' ' for x in cell_row),
            )
            for cell_row in into_groups(row, subgrid_cols)
        ) + f' {NUM_BORDER_CHARS["border"]}'

        if idx != 0 and idx % subgrid_rows == 0:
            rows.append(big_border)

        elif idx not in (0,  height):
            rows.append(mid_border)

        rows.append(formatted_row)

    return f"{top_border}{''.join(rows)}{bot_border}".strip()
