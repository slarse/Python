from data_structures.trie.trie import TrieNode


def test_1():
    """Testing search of particular word in tree"""
    words = ["banana", "bananas", "bandana", "band", "apple", "all", "beast"]
    root = TrieNode()
    root.insert_many(words)
    assert root.find("banana")
    assert root.find("apple")


def test_2():
    """Testing search of particular word in tree"""
    words = ["banana", "bananas", "bandana", "band", "apple", "all", "beast"]
    root = TrieNode()
    root.insert_many(words)
    assert not root.find("bandanas")
    assert not root.find("apps")
