from strings.levenshtein_distance import levenshtein_distance

class TestLevenshteinDistance:
    
    def test_levenshtein_distance_1(self):
        first_word = 'test'
        second_word = 'data'
        result = levenshtein_distance(first_word, second_word)
        assert result == 4
    
    def test_levenshtein_distance_2(self):
        first_word = 'sample'
        second_word = 'set'
        result = levenshtein_distance(first_word, second_word)
        assert result == 5