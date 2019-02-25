from __future__ import absolute_import
from data_structures.union_find.union_find import UnionFind
import pytest

def test_init_with_valid_size():
    '''Testing  for set with valid size'''
    uf = UnionFind(5)
    assert uf.size == 5

def test_init_with_invalid_size_1():
    '''Testing  for set with invalid size'''
    uf = UnionFind(5)
    with pytest.raises(ValueError):
        uf = UnionFind(0)
            
def test_init_with_invalid_size_2():
    '''Testing  for set with invalid size'''
    uf = UnionFind(5)
    with pytest.raises(ValueError):
        uf = UnionFind(-5)

def test_union_with_valid_values():
    '''Testing union for valid set of values'''
    uf = UnionFind(10)

    for i in range(11):
        for j in range(11):
            uf.union(i, j)

def test_union_with_invalid_values_1():
    '''Testing union for invalid set of values'''
    uf = UnionFind(10)
    with pytest.raises(ValueError):
        uf.union(-1, 1)
            
def test_union_with_invalid_values_2():
    '''Testing union for invalid set of values'''
    uf = UnionFind(10)
    with pytest.raises(ValueError):
        uf.union(11, 1)

def test_same_set_with_valid_values_1():
    '''Testing union for valid set of values with the same set'''
    uf = UnionFind(10)

    for i in range(11):
        for j in range(11):
            if i == j:
                assert uf.same_set(i, j) == True
            else:
                assert uf.same_set(i, j) == False

def test_same_set_with_valid_values_2():
    '''Testing union for valid set of values with the same set'''
    uf = UnionFind(10)
    uf.union(1, 2)
    assert uf.same_set(1, 2) == True

    uf.union(3, 4)
    assert uf.same_set(3, 4) == True

    assert uf.same_set(1, 3) == False
    assert uf.same_set(1, 4) == False
    assert uf.same_set(2, 3) == False
    assert uf.same_set(2, 4) == False

    uf.union(1, 3)
    assert uf.same_set(1, 3) == True
    assert uf.same_set(1, 4) == True
    assert uf.same_set(2, 3) == True
    assert uf.same_set(2, 4) == True

    uf.union(4, 10)
    assert uf.same_set(1, 10) == True
    assert uf.same_set(2, 10) == True
    assert uf.same_set(3, 10) == True
    assert uf.same_set(4, 10) == True

def test_same_set_with_invalid_values_1():
    '''Testing union for invalid set of values with the same set'''
    uf = UnionFind(10)
    with pytest.raises(ValueError):
        uf.same_set(-1, 1)
            
def test_same_set_with_invalid_values_2():
    '''Testing union for invalid set of values with the same set'''
    uf = UnionFind(10)
    with pytest.raises(ValueError):
        uf.same_set(11, 0)



