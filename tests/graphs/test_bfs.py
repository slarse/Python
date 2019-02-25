from graphs.BFS import bfs


def test_bfs(sample_graph):
    assert bfs(sample_graph, "A") == set(["A", "B", "C", "D", "E", "F"])
