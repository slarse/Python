from data_structures.graph.even_tree import even_tree
from collections import defaultdict


class TestEvenTree:
    
    def test_even_tree(self):
        n, m = 10, 9
        tree = defaultdict(list)
        visited = {}
        cuts = []
        count = 0
        edges = [
            (2, 1),
            (3, 1),
            (4, 3),
            (5, 2),
            (6, 1),
            (7, 2),
            (8, 6),
            (9, 8),
            (10, 8),
        ]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        even_tree()
        assert (len(cuts) - 1) == 2
