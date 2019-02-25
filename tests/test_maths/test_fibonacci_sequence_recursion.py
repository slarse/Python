from maths import fibonacci_sequence_recursion


def test_less_than_one():
    assert fibonacci_sequence_recursion.recur_fibo(0) == 0


def test_recur_fibo():
    assert fibonacci_sequence_recursion.recur_fibo(10) == 55
