from strings.knuth_morris_pratt import get_failure_array,kmp
    
def test_knuth_morris_pratt_1():
    '''Finding pattern in text1 and text2'''
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert kmp(pattern, text1) and not kmp(pattern, text2)
        
def test_knuth_morris_pratt_2():
    '''Finding pattern in text'''
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert kmp(pattern, text)
    
def test_knuth_morris_pratt_3():
    '''Finding pattern in text'''
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert kmp(pattern, text)
    
def test_knuth_morris_pratt_4():
    '''Finding pattern in text'''
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert kmp(pattern, text)
    
def test_knuth_morris_pratt_5():
    '''Testing the get_failure_array function when comparison fails'''
    pattern = "aabaabaaa"
    assert get_failure_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]