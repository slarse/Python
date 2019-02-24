from other.frequency_finder import englishFreqMatchScore


class TestFrequencyFinder:
    def test_frequency_match_score(self):
        assert englishFreqMatchScore("Hello World") == 1
