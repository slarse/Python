import pytest

from maths import newton_raphson


def test_newton_raphson_positive():
    assert newton_raphson.newton_raphson(lambda x: x) == (0.0, 0.0)


def test_newton_raphson_negative():
    with pytest.raises(ValueError):
        newton_raphson.newton_raphson(lambda x: x * x + 1)
