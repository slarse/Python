from hashes.md5 import md5me


def test_hash_empty_string():
    assert md5me("") == "d41d8cd98f00b204e9800998ecf8427e"


def test_hash_quick_brown_fox():
    assert (
        md5me("The quick brown fox jumps over the lazy dog")
        == "9e107d9d372bb6826bd81d3542a419d6"
    )
