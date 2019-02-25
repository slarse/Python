import pytest

from dynamic_programming import longest_common_subsequence

@pytest.fixture
def expected():
	return (4, ['A', 'G', 'G', 'T', 'A', 'B'])

def test_longest_common_subsequence(expected):
	x = 'AGGTAB'
	y = 'GXTXAYB'
	assert longest_common_subsequence.lcs_dp(x, y) == expected
