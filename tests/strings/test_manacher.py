from strings.manacher import palindromic_string

def test_manacher_1():
    '''Testing if a string is palindromic or not'''
    n = "abba"
    assert palindromic_string(n) == "abba"
    
def test_manacher_2():
    '''Testing if a string is not palindromic then return the center character'''
    n = "qwerty"
    assert palindromic_string(n) == "w"