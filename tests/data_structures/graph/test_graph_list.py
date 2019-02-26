from data_structures.graph.graph_list import Graph


def test_graph_list():
    """Testing the listing function of graph"""
    g = Graph(10)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    for i in g.graph:
        i.sort()
    assert g.graph == [[0, 2], [0, 2], [0, 3, 4], [0, 4], [0], [0], [0], [0], [0], [0]]
