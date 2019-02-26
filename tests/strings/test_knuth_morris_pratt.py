from strings.knuth_morris_pratt import get_failure_array, kmp


def test_knuth_morris_pratt_find_pattern_in_text1_and_text2():
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert kmp(pattern, text1) and not kmp(pattern, text2)


def test_knuth_morris_pratt_find_pattern_in_text_1():
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert kmp(pattern, text)


def test_knuth_morris_pratt_find_pattern_in_text_2():
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert kmp(pattern, text)


def test_knuth_morris_pratt_find_pattern_in_text_3():
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert kmp(pattern, text)


def test_knuth_morris_pratt_get_failure_array():
    pattern = "aabaabaaa"
    assert get_failure_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
