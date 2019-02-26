from data_structures.stacks.infix_to_postfix_conversion import infix_to_postfix

def test_infix_to_postfix_conversion():
    '''Testing conversion of infix to postfix expression'''
    expression = 'a+b*(c^d-e)^(f+g*h)-i'
    assert infix_to_postfix(expression) == "a b c d ^ e - f g h * + ^ * + i -"