from strings.manacher import palindromic_string

class TestManacher:
    
    def test_manacher_1(self):
        n = "abba"
        assert palindromic_string(n) == "abba"
    
    def test_manacher_2(self):
        n = "qwerty"
        assert palindromic_string(n) == "w"