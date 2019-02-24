import pytest

from graphs.articulation_points import computeAP


class TestArticulationPoints:
    @pytest.fixture
    def adjacency_list_graph(self):
        return {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3, 5],
            3: [2, 4],
            4: [3],
            5: [2, 6, 8],
            6: [5, 7],
            7: [6, 8],
            8: [5, 7],
        }

    def test_articulation_points(self, adjacency_list_graph):
        assert sorted(computeAP(adjacency_list_graph)) == [2, 3, 5]
