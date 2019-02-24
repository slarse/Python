from arithmetic_analysis.newton_method import f, f1, newton


class TestNewtonMethod:
    def test_newton_method(self, epsilon):
        x = newton(f, f1, 3)
        assert abs(f(x)) < epsilon
