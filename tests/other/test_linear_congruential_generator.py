import pytest

from other.linear_congruential_generator import LinearCongruentialGenerator


@pytest.fixture
def generator():
    return LinearCongruentialGenerator(1664525, 1013904223, 2 << 31)


def test_generate_numbers(generator):
    """Test that the first ten generated numbers are all unique."""
    numbers = set([generator.next_number() for i in range(10)])
    assert len(numbers) == 10
