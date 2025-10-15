from __future__ import annotations

from typing import List


def first_n_fibonacci(count: int) -> List[int]:
    """
    Return the first `count` Fibonacci numbers starting with 0, 1.

    Edge cases:
    - count < 0: raises ValueError
    - count == 0: returns []
    - count == 1: returns [0]
    - count == 2: returns [0, 1]
    """
    if not isinstance(count, int):
        raise TypeError("count must be an int")

    if count < 0:
        raise ValueError("count must be non-negative")

    # Fast-path small counts for clarity
    if count == 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]

    sequence: List[int] = [0, 1]
    previous_value, current_value = 0, 1
    for _ in range(2, count):
        next_value = previous_value + current_value
        sequence.append(next_value)
        previous_value, current_value = current_value, next_value
    return sequence


__all__ = ["first_n_fibonacci"]


