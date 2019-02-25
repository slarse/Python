from data_structures.trie.trie import TrieNode


class TestTrie:
    
    def test_1(self):
        words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
        root = TrieNode()
        root.insert_many(words)
        assert root.find('banana')
    
    def test_2(self):
        words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
        root = TrieNode()
        root.insert_many(words)
        assert not root.find('bandanas')
        
    def test_3(self):
        words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
        root = TrieNode()
        root.insert_many(words)
        assert not root.find('apps')
    
    def test_4(self):
        words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
        root = TrieNode()
        root.insert_many(words)
        assert root.find('apple')