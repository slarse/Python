from data_structures.binary_tree.AVLtree import AVLtree
import random

class TestAVLTree:
    
    def test_AVL_tree(self):
        t = AVLtree()
        t.traversale()
        l = list(range(10))
        random.shuffle(l)
        for i in l:
            t.insert(i)
            t.traversale()
        assert t.test() == 4
    
    def test_AVL_tree_2(self):
        t = AVLtree()
        t.traversale()
        l = list(range(10))
        random.shuffle(l)
        for i in l:
            t.insert(i)
            t.traversale()   
        random.shuffle(l)
        for i in l:
            t.del_node(i)
            t.traversale()
        assert t.test() == 0