from arithmetic_analysis.intersection import f, intersection


def test_intersection(epsilon):
    x = intersection(f, 3, 3.5)
    assert abs(f(x)) < epsilon
