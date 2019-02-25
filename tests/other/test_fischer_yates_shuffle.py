from other.fischer_yates_shuffle import FYshuffle


def test_shuffle_integers():
    integers = [0, 1, 2, 3, 4, 5, 6, 7]
    original = integers.copy()
    FYshuffle(integers)
    assert sorted(original) == sorted(integers)


def test_shuffle_strings():
    strings = ["python", "says", "hello", "!"]
    original = strings.copy()
    FYshuffle(strings)
    assert sorted(original) == sorted(strings)
