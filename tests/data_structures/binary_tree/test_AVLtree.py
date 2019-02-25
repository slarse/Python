from data_structures.binary_tree.AVLtree import AVLtree
import random
    
def test_AVL_tree_1():
    '''Testing height of the tree after multiple insert in tree'''
    t = AVLtree()
    t.traversale()
    l = list(range(10))
    random.shuffle(l)
    for i in l:
        t.insert(i)
        t.traversale()
    assert t.getheight() == 4
    
def test_AVL_tree_2():
    '''Testing height of tree after insertion and deletion in tree'''
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
    assert t.getheight() == 0