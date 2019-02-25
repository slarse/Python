from dynamic_programming import edit_distance

def test_edit_distance():
	assert edit_distance.EditDistance().solve("haha", "höhö") == 2
