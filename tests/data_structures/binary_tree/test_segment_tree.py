from data_structures.binary_tree.segment_tree import SegmentTree


def test_segment_tree_1():
    """Testing querying of the segment_tree"""
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    segt = SegmentTree(A)
    assert segt.query(4, 6) == 7
    assert segt.query(7, 11) == 14
    assert segt.query(7, 12) == 15


def test_segment_tree_2():
    """Testing querying of the segment_tree after updating data"""
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    segt = SegmentTree(A)
    segt.update(1, 3, 111)
    assert segt.query(1, 15) == 111
