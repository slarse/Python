from graphs.DFS import dfs


class TestDFS:
    def test_dfs(self, sample_graph):
        assert dfs(sample_graph, "A") == set(["A", "B", "C", "D", "E", "F"])
