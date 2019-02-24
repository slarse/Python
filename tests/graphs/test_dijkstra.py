import pytest

from graphs.dijkstra import dijkstra

class TestDijkstra:
    @pytest.fixture
    def dijkstra_graph(self):
        return {"A": [["B", 2], ["C", 5]],
                "B": [["A", 2], ["D", 3], ["E", 1]],
                "C": [["A", 5], ["F", 3]],
                "D": [["B", 3]],
                "E": [["B", 1], ["F", 3]],
                "F": [["C", 3], ["E", 3]]}


    def test_dijkstra(self, dijkstra_graph):
        assert dijkstra(dijkstra_graph, "E", "C") == 6
