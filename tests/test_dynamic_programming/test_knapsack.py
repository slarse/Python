import pytest

from dynamic_programming import knapsack

@pytest.fixture
def params():
	return dict(
		val = [3,2,4,4],
	    wt = [4,3,2,3],
	    n = 4,
	    W = 6
    )

def test_knapsack(params):
	assert knapsack.knapsack(**params) == 8