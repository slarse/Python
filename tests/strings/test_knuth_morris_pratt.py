from strings.knuth_morris_pratt import get_failure_array,kmp

class TestKnuthMorrisPratt:
    
    def test_1(self):
        # Test 1)
        pattern = "abc1abc12"
        text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
        text2 = "alskfjaldsk23adsfabcabc"
        assert kmp(pattern, text1) and not kmp(pattern, text2)
        
    def test_2(self):
        # Test 2)
        pattern = "ABABX"
        text = "ABABZABABYABABX"
        assert kmp(pattern, text)
    
    def test_3(self):
        # Test 3)
        pattern = "AAAB"
        text = "ABAAAAAB"
        assert kmp(pattern, text)
    
    def test_4(self):
        # Test 4)
        pattern = "abcdabcy"
        text = "abcxabcdabxabcdabcdabcy"
        assert kmp(pattern, text)
    
    def test_5(self):
        # Test 5)
        pattern = "aabaabaaa"
        assert get_failure_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]