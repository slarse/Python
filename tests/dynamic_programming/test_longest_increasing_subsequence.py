import pytest

from dynamic_programming import longest_increasing_subsequence

@pytest.mark.parametrize(
	'arg, expected', [
	([4,8,7,5,1,12,2,3,9], [1, 2, 3, 9]), ([9,8,7,6,5,7], [8])
	]
)
def test_longest_increasing_subsequence(arg, expected):
	assert longest_increasing_subsequence.longestSub(arg) == expected
