from other.euclidean_gcd import euclidean_gcd


def test_relatively_prime():
    assert euclidean_gcd(3, 5) == 1


def test_is_symmetric():
    assert euclidean_gcd(3, 5) == euclidean_gcd(5, 3)


def test_not_relatively_prime():
    assert euclidean_gcd(3, 6) == 3
