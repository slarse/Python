import pytest

from arithmetic_analysis.bisection import bisection, f


def test_bisection(epsilon):
    x = bisection(f, 1, 1000)
    assert pytest.approx(f(x), abs=epsilon) == 0
