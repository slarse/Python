import pytest

from graphs.check_bipartite_graph_bfs import checkBipartite


@pytest.fixture
def bipartite_adjacency_list_graph():
    return {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}


def test_is_bipartite(bipartite_adjacency_list_graph):
    assert checkBipartite(bipartite_adjacency_list_graph)
