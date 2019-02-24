import pytest

from searches import sentinel_linear_search


@pytest.fixture
def sorted_list():
    return [0, 5, 7, 10, 15]


@pytest.fixture
def search_items():
    return [0, 15, 5]


@pytest.fixture
def expected_returns():
    return [0, 4, 1]


def test_linear_search(sorted_list, search_items, expected_returns):
    """Test that sentinel_linear_search finds its targets in sorted lists that contain them"""
    for item, expected_return in zip(search_items, expected_returns):
        assert (
            sentinel_linear_search.sentinel_linear_search(sorted_list, item)
            == expected_return
        )


def test_linear_search_returns_none_if_target_not_in_list(sorted_list):
    """Test that sentinel_linear_search returns None if its target is not in the list"""
    assert sentinel_linear_search.sentinel_linear_search(sorted_list, 6) == None
