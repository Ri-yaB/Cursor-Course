from typing import List


def fibonacci_sequence(n: int) -> List[int]:
    """
    Return the first n Fibonacci numbers starting from 0.

    The sequence is defined as:
    F(0) = 0, F(1) = 1
    F(k) = F(k-1) + F(k-2) for k >= 2

    Args:
        n: Number of terms to generate. If n <= 0, returns [].

    Returns:
        List of length n with the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence: List[int] = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
