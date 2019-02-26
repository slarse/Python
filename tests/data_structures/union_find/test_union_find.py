from __future__ import absolute_import
from data_structures.union_find.union_find import UnionFind
import pytest


def test_init_with_valid_size():
    """Testing  for set with valid size"""
    uf = UnionFind(5)
    assert uf.size == 5


def test_union_with_valid_values():
    """Testing union for valid set of values"""
    uf = UnionFind(10)

    for i in range(11):
        for j in range(11):
            uf.union(i, j)


def test_same_set_with_valid_values_1():
    """Testing union for valid set of values with the same set"""
    uf = UnionFind(10)

    for i in range(11):
        for j in range(11):
            if i == j:
                assert uf.same_set(i, j)
            else:
                assert not uf.same_set(i, j)


def test_same_set_with_valid_values_2():
    """Testing union for valid set of values with the same set"""
    uf = UnionFind(10)
    uf.union(1, 2)
    assert uf.same_set(1, 2)

    uf.union(3, 4)
    assert uf.same_set(3, 4)

    assert not uf.same_set(1, 3)
    assert not uf.same_set(1, 4)
    assert not uf.same_set(2, 3)
    assert not uf.same_set(2, 4)

    uf.union(1, 3)
    assert uf.same_set(1, 3)
    assert uf.same_set(1, 4)
    assert uf.same_set(2, 3)
    assert uf.same_set(2, 4)

    uf.union(4, 10)
    assert uf.same_set(1, 10)
    assert uf.same_set(2, 10)
    assert uf.same_set(3, 10)
    assert uf.same_set(4, 10)
