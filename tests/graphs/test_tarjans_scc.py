import pytest

from graphs.tarjans_scc import create_graph, tarjan


@pytest.fixture
def tarjan_graph():
    n_vertices = 7
    source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    edges = [(u, v) for u, v in zip(source, target)]
    return create_graph(n_vertices, edges)


def test_tarjan(tarjan_graph):
    sccs = [sorted(scc) for scc in sorted(tarjan(tarjan_graph))]
    assert sccs == [[0, 1, 2, 3], [4], [5], [6]]
