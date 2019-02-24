import pytest

from graphs.kahns_algorithm_long import longestDistance


@pytest.fixture
def adjacency_list_graph():
    return {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}


def test_kahns_algorithm_long(adjacency_list_graph):
    assert longestDistance(adjacency_list_graph) == 5
