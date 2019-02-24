from arithmetic_analysis.intersection import f, intersection


class TestIntersection:
    def test_intersection(self, epsilon):
        x = intersection(f, 3, 3.5)
        assert abs(f(x)) < epsilon
