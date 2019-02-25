from data_structures.binary_tree.binary_search_tree import BinarySearchTree, InPreOrder

class TestBinarySearchTree():
    
    def test_binary_search_tree_1(self):
        t = BinarySearchTree()
        t.insert(8)
        t.insert(3)
        t.insert(6)
        t.insert(1) 
        assert t.getNode(6) is not None
    
    def test_binary_search_tree_2(self):
        t = BinarySearchTree()
        t.insert(10)
        t.insert(14)
        t.insert(13)
        t.insert(4)
        t.insert(7)
        assert t.getNode(-1) is None
    
    def test_binary_search_tree_3(self):
        t = BinarySearchTree()
        t.insert(10)
        t.insert(14)
        t.insert(13)
        t.insert(4)
        t.insert(7)    
        if(not t.empty()):
            assert t.getMax().getLabel() == 14
    
    def test_binary_search_tree_4(self):
        t = BinarySearchTree()
        t.insert(1)
        t.insert(10)
        t.insert(14)
        t.insert(13)
        if(not t.empty()):
            assert t.getMin().getLabel() == 1
    
    def test_binary_search_tree_5(self):
        t = BinarySearchTree()
        t.insert(8)
        t.insert(3)
        t.insert(6)
        t.insert(1)
        t.insert(10)
        t.insert(14)
        t.insert(13)
        t.insert(4)
        t.insert(7)
        t.delete(13)
        t.delete(10)
        t.delete(8)
        t.delete(3)
        t.delete(6)
        t.delete(14)
        list = t.traversalTree(InPreOrder, t.root)
        assert list == [7,1,4]