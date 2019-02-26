from data_structures.binary_tree.fenwick_tree import FenwickTree


def test_fenwick_tree_1():
    """Testing the query of data in Fenwick Tree"""
    f = FenwickTree(100)
    f.update(1, 20)
    f.update(4, 4)
    assert f.query(1) == 20
    assert f.query(3) == 20
    assert f.query(4) == 24


def test_fenwick_tree_2():
    """Testing the query of data in Fenwick Tree"""
    f = FenwickTree(100)
    f.update(1, 20)
    f.update(4, 4)
    f.update(2, -5)
    assert f.query(1) == 20
    assert f.query(3) == 15
