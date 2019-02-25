from data_structures.stacks.stock_span_problem import calculateSpan

def test_stock_span_problem():
    '''Testing the stock span function'''
    price = [10, 4, 5, 90, 120, 80] 
    S = [0 for i in range(len(price)+1)] 
    calculateSpan(price, S) 
    assert S == [1,1,2,4,5,1,0]