import pytest

from m1v3 import first_n_fibonacci


@pytest.mark.parametrize(
    "count,expected",
    [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (3, [0, 1, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ],
)
def test_first_n_fibonacci_basic_and_small(count, expected):
    assert first_n_fibonacci(count) == expected


def test_first_n_fibonacci_type_and_value_errors():
    with pytest.raises(TypeError):
        first_n_fibonacci(3.14)  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        first_n_fibonacci("5")  # type: ignore[arg-type]

    with pytest.raises(ValueError):
        first_n_fibonacci(-1)
