from data_structures.graph.graph import AdjacencyList

class TestGraph:
    
    def test_graph(self):
        al = AdjacencyList()
        al.addEdge(0, 1)
        al.addEdge(0, 4)
        al.addEdge(4, 1)
        al.addEdge(4, 3)
        al.addEdge(1, 0)
        al.addEdge(1, 4)
        al.addEdge(1, 3)
        al.addEdge(1, 2)
        al.addEdge(2, 3)
        al.addEdge(3, 4)
        assert al.List == {0: [1, 4], 4: [1, 3], 1: [0, 4, 3, 2], 2: [3], 3: [4]}
