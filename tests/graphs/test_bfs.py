from graphs.BFS import bfs


class TestBFS:
    def test_bfs(self, sample_graph):
        assert bfs(sample_graph, "A") == set(["A", "B", "C", "D", "E", "F"])
