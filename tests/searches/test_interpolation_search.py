import pytest

from searches import interpolation_search


def test_assert_sorted_on_sorted_list():
    """Test that __assert_sorted returns True on a sorted list"""
    sorted_list = [0, 1, 2, 4]
    assert interpolation_search.__assert_sorted(sorted_list)


def test_assert_sorted_raises_on_unsorted_list():
    """Test that __assert_sorted raises ValueError on an unsorted list"""
    unsorted_list = [10, -1, 5]
    with pytest.raises(ValueError):
        assert interpolation_search.__assert_sorted(unsorted_list)
