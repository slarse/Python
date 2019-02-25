import pytest

from ciphers import simple_substitution_cipher


@pytest.fixture
def plaintext():
    return "Harshil Darji"


@pytest.fixture
def ciphertext():
    return "Ilcrism Olcvs"


@pytest.fixture
def key():
    return "LFWOAYUISVKMNXPBDCRJTQEGHZ"


def test_encrypt_message(plaintext, ciphertext, key):
    """Test that encryptMessage returns expected ciphertext"""
    assert ciphertext == simple_substitution_cipher.encryptMessage(key, plaintext)


def test_decrypt_message(plaintext, ciphertext, key):
    """Test that encryptMessage returns expected ciphertext"""
    assert plaintext == simple_substitution_cipher.decryptMessage(key, ciphertext)
