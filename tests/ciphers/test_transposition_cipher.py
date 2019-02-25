import pytest

from ciphers import transposition_cipher


@pytest.fixture
def plaintext():
    return "Harshil Darji"


@pytest.fixture
def ciphertext():
    return "Hlia rDsahrij"


@pytest.fixture
def key():
    return 6


def test_encrypt_message(plaintext, ciphertext, key):
    """Test that encryptMessage returns expected ciphertext"""
    assert ciphertext == transposition_cipher.encryptMessage(key, plaintext)


def test_decrypt_message(plaintext, ciphertext, key):
    """Test that encryptMessage returns expected ciphertext"""
    assert plaintext == transposition_cipher.decryptMessage(key, ciphertext)
