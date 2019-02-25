from data_structures.graph.graph_matrix import Graph

class TestGraphMatrix:
    
    def test_graph_matrix(self):
        g = Graph(10)
        g.add_edge(1,4)
        g.add_edge(4,2)
        g.add_edge(4,5)
        g.add_edge(2,5)
        g.add_edge(5,3)
        assert g.graph == [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]