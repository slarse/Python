from strings.levenshtein_distance import levenshtein_distance

def test_levenshtein_distance_1():
    '''Testing levenshtein distance for test and data string values'''
    first_word = 'test'
    second_word = 'data'
    result = levenshtein_distance(first_word, second_word)
    assert result == 4
    
def test_levenshtein_distance_2():
    '''Testing levenshtein distance for sample and set string values'''
    first_word = 'sample'
    second_word = 'set'
    result = levenshtein_distance(first_word, second_word)
    assert result == 5