import pytest

from dynamic_programming import matrix_chain_order

@pytest.fixture
def expected():
	return [[0, 0, 0], [0, 0, 6], [0, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]]


def test_matrix_chain_order(expected):
	assert matrix_chain_order.MatrixChainOrder([1,2,3]) == expected
