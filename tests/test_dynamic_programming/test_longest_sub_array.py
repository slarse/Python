from dynamic_programming import longest_sub_array

def test_longest_sub_array():
	assert longest_sub_array.SubArray("1,2,3,4").solve_sub_array() == 10
