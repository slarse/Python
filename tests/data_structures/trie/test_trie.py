from data_structures.trie.trie import TrieNode

def test_1():
    '''Testing search of particular word in tree'''
    words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
    root = TrieNode()
    root.insert_many(words)
    assert root.find('banana')
    
def test_2():
    '''Testing search of particular word in tree'''
    words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
    root = TrieNode()
    root.insert_many(words)
    assert not root.find('bandanas')
        
def test_3():
    '''Testing search of particular word in tree'''
    words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
    root = TrieNode()
    root.insert_many(words)
    assert not root.find('apps')
    
def test_4():
    '''Testing search of particular word in tree'''
    words = ['banana', 'bananas', 'bandana', 'band', 'apple', 'all', 'beast']
    root = TrieNode()
    root.insert_many(words)
    assert root.find('apple')