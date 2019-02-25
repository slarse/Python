import os
from contextlib import contextmanager

import pytest

from ciphers import xor_cipher


@contextmanager
def _cd(newdir):
    """Context for changing cwd"""
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


@pytest.fixture
def key():
    return 67


@pytest.fixture
def plaintext():
    return "hallo welt"


@pytest.fixture
def textfile(tmpdir):
    f = tmpdir.join("test.txt")
    f.write(plaintext)
    return f


def test_encrypt_decrypt_returns_a_char_list_of_the_plaintext(key, plaintext):
    """Test that encrypt followed by decrypt returns the plaintext as a list of chars"""
    crypt = xor_cipher.XORCipher()
    assert list(plaintext) == crypt.decrypt(crypt.encrypt(plaintext, key), key)


def test_encrypt_decrypt_string_is_a_no_op(key, plaintext):
    """Test that encrypt_string followed by decrypt_string returns the plaintext"""
    crypt = xor_cipher.XORCipher()
    assert plaintext == crypt.decrypt_string(crypt.encrypt_string(plaintext, key), key)


def test_encrypt_file_doesnt_crash(key, textfile, tmpdir):
    """Test that encrypting a file doesn't crash"""
    with _cd(tmpdir):
        crypt = xor_cipher.XORCipher()
        success = crypt.encrypt_file(os.path.abspath(textfile), key)
    assert success


def test_decrypt_file_doesnt_crash(key, textfile, tmpdir):
    """Test that decrypting a file doesn't crash"""
    with _cd(tmpdir):
        crypt = xor_cipher.XORCipher()
        success = crypt.decrypt_file(os.path.abspath(textfile), key)
    assert success
