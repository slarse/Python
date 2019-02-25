from data_structures.graph.breadth_first_search import Graph

class TestBreadthFirstSearch:
    
    def test_bfs(self):
        g = Graph()
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(3, 3)
        g.BFS(2)
        assert g.vertex == {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}