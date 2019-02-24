from ciphers import onepad_cipher


def test_encrypt_decrypt_is_a_no_op():
    """Test that encrypting followed by decrypting returns the plaintext"""
    plaintext = "Hello"
    c, k = onepad_cipher.Onepad().encrypt(plaintext)
    assert plaintext == onepad_cipher.Onepad().decrypt(c, k)
