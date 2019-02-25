from data_structures.stacks.infix_to_postfix_conversion import infix_to_postfix

class TestInfixToPostfixConversion:
    
    def test_infix_to_postfix_conversion(self):
        expression = 'a+b*(c^d-e)^(f+g*h)-i'
        assert infix_to_postfix(expression) == "a b c d ^ e - f g h * + ^ * + i -"