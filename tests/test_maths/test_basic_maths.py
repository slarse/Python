import pytest

from maths import basic_maths


@pytest.mark.parametrize(
    "functioncall, expected",
    [
        (basic_maths.primeFactors(100), [2, 2, 5, 5]),
        (basic_maths.numberOfDivisors(100), 9),
        (basic_maths.sumOfDivisors(100), 217),
        (basic_maths.eulerPhi(100), 40),
    ],
)
def test_basic_maths(functioncall, expected):
    assert functioncall == expected
