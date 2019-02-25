import pytest

from ciphers import affine_cipher


@pytest.fixture
def plaintext():
    return "The affine cipher is a type of monoalphabetic substitution cipher."


@pytest.fixture
def encrypted():
    return "VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi"


@pytest.fixture
def key():
    return 4545


def test_encrypt_message(plaintext, encrypted, key):
    """Test that encryption returns expected encryption"""
    assert encrypted == affine_cipher.encryptMessage(key, plaintext)
