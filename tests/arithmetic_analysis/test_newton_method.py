import pytest

from arithmetic_analysis.newton_method import f, f1, newton


def test_newton_method(epsilon):
    x = newton(f, f1, 3)
    assert pytest.approx(f(x), abs=epsilon) == 0
