import pytest

from maths import PrimeCheck


@pytest.mark.parametrize("arg, expected", [(37, True), (100, False), (77, True)])
def test_primeCheck(arg, expected):
    PrimeCheck.primeCheck(arg) == expected
