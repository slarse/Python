from strings.levenshtein_distance import levenshtein_distance


def test_levenshtein_distance_between_test_and_data():
    first_word = "test"
    second_word = "data"
    result = levenshtein_distance(first_word, second_word)
    assert result == 4


def test_levenshtein_distance_between_sample_and_set():
    first_word = "sample"
    second_word = "set"
    result = levenshtein_distance(first_word, second_word)
    assert result == 5
