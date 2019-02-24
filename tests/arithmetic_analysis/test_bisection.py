from arithmetic_analysis.bisection import bisection, f


def test_bisection(epsilon):
    x = bisection(f, 1, 1000)
    assert abs(f(x)) < epsilon
