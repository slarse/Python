from dynamic_programming import coin_change

def test_coin_change():
	assert coin_change.dp_count([1, 2, 3], 3, 4) == 4
	assert coin_change.dp_count([2, 5, 3, 6], 4, 10) == 5
