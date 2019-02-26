from strings.manacher import palindromic_string


def test_manacher_find_palindromic_string():
    n = "abba"
    assert palindromic_string(n) == "abba"


def test_manacher_return_output_from_center():
    n = "qwerty"
    assert len(palindromic_string(n)) == 1
    assert palindromic_string(n) in n
