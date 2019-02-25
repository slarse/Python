from data_structures.binary_tree.lazy_segment_tree import SegmentTree

def test_lazt_segment_tree_1():
    '''Testing the querying method on lazy_segment_tree'''
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(N)
    segt.build(1,1,N,A)
    assert segt.query(1,1,N,4,6) == 7
    
def test_lazy_segment_tree_2():
    '''Testing the querying method on lazy_segment_tree'''
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(N)
    segt.build(1,1,N,A)
    assert segt.query(1,1,N,7,11) == 14
    
def test_lazy_segment_tree_3():
    '''Testing the querying method on lazy_segment_tree'''
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(N)
    segt.build(1,1,N,A)
    assert segt.query(1,1,N,7,12) == 15
    
def test_lazy_segment_tree_4():
    '''Testing the querying method on lazy_segment_tree'''
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(N)
    segt.build(1,1,N,A)
    segt.update(1,1,N,1,3,111)
    assert segt.query(1,1,N,1,15) == 111
    