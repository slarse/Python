import numpy
import pytest

from arithmetic_analysis.lu_decomposition import LUDecompose


@pytest.fixture
def decomposition_matrix():
    return numpy.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])

@pytest.fixture
def lower_triangular_matrix():
    return numpy.array([[1, 0, 0], [0, 1, 0], [2.5, 0, 1]])

@pytest.fixture
def upper_triangular_matrix():
    return numpy.array([[2, -2, 1], [0, 1, 2], [0, 8, -1.5]])

def test_decomposition(
    decomposition_matrix, lower_triangular_matrix, upper_triangular_matrix
):
    L, U = LUDecompose(decomposition_matrix)
    assert (L == lower_triangular_matrix).all()
    assert (U == upper_triangular_matrix).all()
