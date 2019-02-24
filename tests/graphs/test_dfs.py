from graphs.DFS import dfs


def test_dfs(sample_graph):
    assert dfs(sample_graph, "A") == set(["A", "B", "C", "D", "E", "F"])
