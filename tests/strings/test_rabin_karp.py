from strings.rabin_karp import rabin_karp


def test_rabin_karp_find_pattern_in_text1_and_text2():
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert rabin_karp(pattern, text1) and not rabin_karp(pattern, text2)


def test_rabin_karp_find_pattern_in_text_1():
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert rabin_karp(pattern, text)


def test_rabin_karp_find_pattern_in_text_2():
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert rabin_karp(pattern, text)


def test_rabin_karp_find_pattern_in_text_3():
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(pattern, text)
