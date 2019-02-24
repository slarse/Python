from other.frequency_finder import englishFreqMatchScore


def test_frequency_match_score():
    assert englishFreqMatchScore("Hello World") == 1
