from data_structures.binary_tree.segment_tree import SegmentTree

class TestSegmentTree:
    
    def test_segment_tree_1(self):
        A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
        segt = SegmentTree(A)
        assert segt.query(4, 6) == 7
        
    def test_segment_tree_2(self):
        A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
        segt = SegmentTree(A)
        assert segt.query(7, 11) == 14
    
    def test_segment_tree_3(self):
        A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
        segt = SegmentTree(A)
        assert segt.query(7, 12) == 15
    
    def test_segment_tree_4(self):
        A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
        segt = SegmentTree(A)
        segt.update(1,3,111)
        assert segt.query(1, 15) == 111
    
        