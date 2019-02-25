from data_structures.stacks.balanced_parentheses import balanced_parentheses

def test_balanced_parentheses_1():
    '''Testing if parentheses are balanced or not'''
    example = '((()))'
    assert balanced_parentheses(example) == True
    
def test_balanced_parentheses_2():
    '''Testing if parentheses are balanced or not'''
    example = '((())'
    assert balanced_parentheses(example) == False
    
def test_balanced_parentheses_3():
    '''Testing if parentheses are balanced or not'''
    example = '(()))'
    assert balanced_parentheses(example) == False
    
    