from maths import segmented_sieve


def test_sieve():
    assert segmented_sieve.sieve(10 ** 6)[-5:] == [
        999953,
        999959,
        999961,
        999979,
        999983,
    ]
