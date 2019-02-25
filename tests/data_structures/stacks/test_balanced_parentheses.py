from data_structures.stacks.balanced_parentheses import balanced_parentheses

class TestBalancedParentheses:
    
    def test_balanced_parentheses_1(self):
        example = '((()))'
        assert balanced_parentheses(example) == True
    
    def test_balanced_parentheses_2(self):
        example = '((())'
        assert balanced_parentheses(example) == False
    
    def test_balanced_parentheses_3(self):
        example = '(()))'
        assert balanced_parentheses(example) == False
    
    