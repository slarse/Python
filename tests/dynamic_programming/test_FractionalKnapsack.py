from dynamic_programming import FractionalKnapsack

def test_FractionalKnapsack():
	assert FractionalKnapsack.fracKnapsack([60, 100, 120],[10, 20, 30],50,3) == 240
