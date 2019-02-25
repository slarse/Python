from data_structures.stacks.stack import Stack

def test_stack_1():
    '''Testing the stack creation'''
    stack = Stack()
    for i in range(10):
        stack.push(i)
        
    assert stack.stack == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
def test_stack_2():
    '''Testing stack pop function'''
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert stack.pop() == 9
    
def test_stack_3():
    '''Testing the peek function of stack'''
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert stack.peek() == 9
    
def test_stack_4():
    '''Testing the peek function of stack for a recently added element'''
    stack = Stack()
    for i in range(10):
        stack.push(i)
    stack.pop()
    stack.push(100)
    assert stack.peek() == 100
    
def test_stack_5():
    '''Testing is stack is empty or not'''
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert stack.is_empty() == False
    
def test_stack_6():
    '''Testing for size of stack'''
    stack = Stack()
    for i in range(10):
        stack.push(i)
    assert stack.size() == 10