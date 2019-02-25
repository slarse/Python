from maths import sieve_of_eratosthenes


def test_sieve():
    sieve_of_eratosthenes.sieve(10) == [2, 3, 5, 7]
