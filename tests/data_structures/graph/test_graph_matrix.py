from data_structures.graph.graph_matrix import Graph

def test_graph_matrix():
    '''Testing the graph matrix generation function'''
    g = Graph(10)
    g.add_edge(1,4)
    g.add_edge(4,2)
    g.add_edge(4,5)
    g.add_edge(2,5)
    g.add_edge(5,3)
    assert g.graph == [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]