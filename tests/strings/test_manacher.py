from strings.manacher import palindromic_string


def test_manacher_find_palindromic_string():
    """Testing if a string is palindromic or not"""
    n = "abba"
    assert palindromic_string(n) == "abba"


def test_manacher_return_output_from_center():
    """Testing if a string is not palindromic then return the center character"""
    n = "qwerty"
    assert palindromic_string(n) == "w"
    assert len(palindromic_string(n)) == 1
    assert palindromic_string(n) in n
