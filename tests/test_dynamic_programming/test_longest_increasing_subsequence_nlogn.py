from dynamic_programming import longest_increasing_subsequence_nlogn

def test_longest_increasing_subsequence_nlogn():
	v = [2, 5, 3, 7, 11, 8, 10, 13, 6]
	assert longest_increasing_subsequence_nlogn.LongestIncreasingSubsequenceLength(v) == 6