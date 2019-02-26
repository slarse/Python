from dynamic_programming import fibonacci

def test_fibonacci():
	assert fibonacci.Fibonacci(10).get(5) == [0, 1, 1, 2, 3, 5]
