import pytest

from other.palindrome import is_palindrome, recursive_palindrome


class TestPalindrome:
    @pytest.fixture
    def palindrome(self):
        return "ama"

    def test_recursive_is_palindrome(self, palindrome):
        assert recursive_palindrome(palindrome)

    def test_regular_is_palindrome(self, palindrome):
        assert is_palindrome(palindrome)
