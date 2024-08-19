"""Global sudoku config."""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from enum import IntEnum, auto
from typing import TypeVar

SudokuBoard = Sequence[MutableSequence[int]]
T = TypeVar('T')

EMPTY_SLOT = 0


class InsertionMode(IntEnum):
    """Rules for inserting numbers."""

    RELAXED = auto()
    STRICT = auto()
