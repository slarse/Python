from maths import modular_exponential


def test_modularExponential():
    assert modular_exponential.modularExponential(3, 200, 13) == 9
