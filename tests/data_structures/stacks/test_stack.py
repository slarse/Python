from data_structures.stacks.stack import Stack

class TestStack:
    
    def test_stack_1(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        
        assert stack.stack == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_stack_2(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        assert stack.pop() == 9
    
    def test_stack_3(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        assert stack.peek() == 9
    
    def test_stack_4(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        stack.pop()
        stack.push(100)
        assert stack.peek() == 100
    
    def test_stack_5(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        assert stack.is_empty() == False
    
    def test_stack_6(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        assert stack.size() == 10