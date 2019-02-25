import pytest

from maths import simpson_rule


def test_simpson_rule():
    a = 0.0
    b = 1.0
    steps = 10.0
    boundary = [a, b]
    y = simpson_rule.method_2(boundary, steps)
    assert y == pytest.approx(1.0 / 3)
