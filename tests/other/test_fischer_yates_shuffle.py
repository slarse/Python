from other.fischer_yates_shuffle import FYshuffle


class TestFischerYatesShuffle:
    def test_shuffle_integers(self):
        integers = [0, 1, 2, 3, 4, 5, 6, 7]
        original = integers.copy()
        FYshuffle(integers)
        assert sorted(original) == sorted(integers)

    def test_shuffle_strings(self):
        strings = ["python", "says", "hello", "!"]
        original = strings.copy()
        FYshuffle(strings)
        assert sorted(original) == sorted(strings)
