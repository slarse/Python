import pytest

from maths import trapezoidal_rule


def test_trapezoidal_rule():
    a = 0.0
    b = 1.0
    steps = 10.0
    boundary = [a, b]
    y = trapezoidal_rule.method_1(boundary, steps)
    assert y == pytest.approx(1.0 / 3, abs=1e-2)
