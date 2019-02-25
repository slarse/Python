from data_structures.stacks.balanced_parentheses import balanced_parentheses


def test_balanced_parentheses_1():
    """Testing if parentheses are balanced or not"""
    example = "((()))"
    assert balanced_parentheses(example)


def test_balanced_parentheses_2():
    """Testing if parentheses are balanced or not"""
    example = "((())"
    assert not balanced_parentheses(example)


def test_balanced_parentheses_3():
    """Testing if parentheses are balanced or not"""
    example = "(()))"
    assert not balanced_parentheses(example)
