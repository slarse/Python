import pytest

from dynamic_programming import fastfibonacci

def test_fastfibonacci():
	assert fastfibonacci.fibonacci(100) == 354224848179261915075

def test_fastfibonacci_raises():
	with pytest.raises(ValueError):
		fastfibonacci.fibonacci(-1)
