import pytest

from searches import jump_search


def test_jump_search_finds_target_in_sorted_list(capsys):
    """Test that jump search finds its target in a sorted list that contains it"""
    expected_index = 10
    jump_search.main()
    captured = capsys.readouterr()
    assert "Number 55 is at index 10" in captured.out
