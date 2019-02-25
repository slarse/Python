import pytest

from binary_tree.basic_binary_tree import depth_of_tree, is_full_binary_tree, Node


@pytest.fixture
def binary_tree():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    return tree


def test_is_not_full_binary_tree(binary_tree):
    assert not is_full_binary_tree(binary_tree)


def test_depth_of_binary_tree(binary_tree):
    assert depth_of_tree(binary_tree) == 5
