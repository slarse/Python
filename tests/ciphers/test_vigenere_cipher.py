import pytest

from ciphers import vigenere_cipher


@pytest.fixture
def plaintext():
    return "This is Harshil Darji from Dharmaj."


@pytest.fixture
def ciphertext():
    return "Akij ra Odrjqqs Gaisq muod Mphumrs."


@pytest.fixture
def key():
    return "HDarji"


def test_encrypt_message(plaintext, ciphertext, key):
    """Test that encryptMessage returns expected ciphertext"""
    assert ciphertext == vigenere_cipher.encryptMessage(key, plaintext)


def test_decrypt_message(plaintext, ciphertext, key):
    """Test that encryptMessage returns expected ciphertext"""
    assert plaintext == vigenere_cipher.decryptMessage(key, ciphertext)
