from data_structures.graph.breadth_first_search import Graph


def test_bfs():
    """Testing breath_first_search with a sample graph"""
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.BFS(2)
    for i in g.vertex:
        g.vertex[i].sort()
    assert g.vertex == {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
