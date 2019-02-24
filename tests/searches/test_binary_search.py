import pytest

from searches import binary_search


@pytest.fixture
def sorted_list():
    return [0, 5, 7, 10, 15]


@pytest.fixture
def search_items():
    return [0, 15, 5]


@pytest.fixture
def expected_returns():
    return [0, 4, 1]


def test_binary_search_finds_target(sorted_list, search_items, expected_returns):
    """Test that binary_search finds its targets in sorted lists that contain them"""
    for item, expected_return in zip(search_items, expected_returns):
        assert binary_search.binary_search(sorted_list, item) == expected_return


def test_binary_search_returns_none_if_target_not_in_list(sorted_list):
    """Test that binary_search returns None if its target is not in the list"""
    assert binary_search.binary_search(sorted_list, 6) == None


def test_binary_search_std_lib(sorted_list, search_items, expected_returns):
    """Test that binary_searc_std_libh finds its targets in sorted lists that contain them"""
    for item, expected_return in zip(search_items, expected_returns):
        assert binary_search.binary_search_std_lib(sorted_list, item) == expected_return


def test_binary_search_std_lib_returns_none_if_target_not_in_list(sorted_list):
    """Test that binary_search_std_lib returns None if its target is not in the list"""
    assert binary_search.binary_search_std_lib(sorted_list, 6) == None


def test_binary_search_by_recursion(sorted_list, search_items, expected_returns):
    """Test that binary_search_by_recursion returns expected values"""
    for item, expected_return in zip(search_items, expected_returns):
        assert binary_search.binary_search_by_recursion(sorted_list, item, 0, len(sorted_list) - 1) == expected_return


def test_binary_search_by_recursion_returns_none_if_target_not_in_list(sorted_list):
    """Test that binary_search_by_recursion returns None if its target is not in the list"""
    assert binary_search.binary_search_by_recursion(sorted_list, 6, 0, len(sorted_list) - 1) == None


def test_binary_search_returns_none_if_target_not_in_list(sorted_list):
    """Test that binary_search returns None if its target is not in the list"""
    assert binary_search.binary_search(sorted_list, 6) == None


def test_assert_sorted_on_sorted_list(sorted_list):
    """Test that __assert_sorted returns True on a sorted list"""
    assert binary_search.__assert_sorted(sorted_list)


def test_assert_sorted_raises_on_unsorted_list():
    """Test that __assert_sorted raises ValueError on an unsorted list"""
    unsorted_list = [10, -1, 5]
    with pytest.raises(ValueError):
        assert binary_search.__assert_sorted(unsorted_list)
