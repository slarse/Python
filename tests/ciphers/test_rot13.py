from ciphers import rot13


def test_dencrypt():
    """Test that dencrypt returns expected values"""
    s0 = "HELLO"
    s1 = rot13.dencrypt(s0, 13)
    s2 = rot13.dencrypt(s1, 13)
    assert s1 == "URYYB"
    assert s2 == "HELLO"
