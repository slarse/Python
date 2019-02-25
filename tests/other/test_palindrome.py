import pytest

from other.palindrome import is_palindrome, recursive_palindrome


@pytest.fixture
def palindrome():
    return "ama"


def test_recursive_is_palindrome(palindrome):
    assert recursive_palindrome(palindrome)


def test_regular_is_palindrome(palindrome):
    assert is_palindrome(palindrome)
