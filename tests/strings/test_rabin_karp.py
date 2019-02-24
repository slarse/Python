from strings.rabin_karp import rabin_karp

class TestRabinKarp:
    
    def test_1(self):
        # Test 1)
        pattern = "abc1abc12"
        text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
        text2 = "alskfjaldsk23adsfabcabc"
        assert rabin_karp(pattern, text1) and not rabin_karp(pattern, text2)
    
    def test_2(self):
        # Test 2)
        pattern = "ABABX"
        text = "ABABZABABYABABX"
        assert rabin_karp(pattern, text)
    
    def test_3(self):
        # Test 3)
        pattern = "AAAB"
        text = "ABAAAAAB"
        assert rabin_karp(pattern, text)
    
    def test_4(self):
        # Test 4)
        pattern = "abcdabcy"
        text = "abcxabcdabxabcdabcdabcy"
        assert rabin_karp(pattern, text)