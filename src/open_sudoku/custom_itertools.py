"""Customised iteration tools."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Sequence

    from open_sudoku.config import T


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
