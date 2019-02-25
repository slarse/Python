import pytest

from matrix import matrix_multiplication_addition

@pytest.fixture
def matrices():
	return dict(
		matrix_a = [[12, 10], [3, 9]],
		matrix_b = [[3, 4], [7, 4]]
		)
@pytest.fixture
def expected_add():
	return [[15, 14], [10, 13]]

@pytest.fixture
def expected_multiply():
	return [[106, 88], [72, 48]]

def test_add(matrices, expected_add):
	assert matrix_multiplication_addition.add(
		**matrices
		) == expected_add

def test_multiply(matrices, expected_multiply):
	assert matrix_multiplication_addition.multiply(
		**matrices
		) == expected_multiply