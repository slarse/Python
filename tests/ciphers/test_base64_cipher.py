from ciphers import base64_cipher


def test_encrypt_decrypt_is_a_no_op():
    """Test that encrypting followed by a decryption returns the plaintext"""
    plaintext = "WELCOME to base64 encoding"
    assert plaintext == base64_cipher.decodeBase64(
        base64_cipher.encodeBase64(plaintext)
    )
