import pytest

from graphs.kahns_algorithm_topo import topologicalSort


@pytest.fixture
def adjacency_list_graph():
    return {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}


def test_kahns_algorithm_topo(adjacency_list_graph):
    assert topologicalSort(adjacency_list_graph) == [0, 1, 2, 3, 4, 5]
