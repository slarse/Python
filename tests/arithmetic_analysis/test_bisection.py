from arithmetic_analysis.bisection import bisection, f


class TestBisection:
    def test_bisection(self, epsilon):
        x = bisection(f, 1, 1000)
        assert abs(f(x)) < epsilon
