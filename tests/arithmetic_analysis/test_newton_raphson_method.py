from math import sqrt
import pytest
from pytest import approx

from arithmetic_analysis.newton_raphson_method import NewtonRaphson


class TestNewtonRaphsonMethod:
    def test_trigonometric_function(self):
        assert NewtonRaphson("sin(x)", 2) == approx(2)

    def test_polynomial_root(self):
        x = NewtonRaphson("x**2 - 5*x + 2", 0.4)
        first_root = 2.5 + 0.5 * sqrt(17)
        second_root = 2.5 - 0.5 * sqrt(17)
        assert x == approx(first_root) or x == approx(second_root)

    def test_square_root_five(self):
        assert NewtonRaphson("x**2 - 5", 0.1) == approx(sqrt(5))

    def test_exponential_root(self):
        assert NewtonRaphson("exp(x) - 1", 0) == approx(0)
