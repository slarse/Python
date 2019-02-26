import pytest

from dynamic_programming import floyd_warshall

@pytest.fixture
def graph():
	graph = floyd_warshall.Graph(5)
	graph.addEdge(0,2,9)
	graph.addEdge(0,4,10)
	graph.addEdge(1,3,5)
	graph.addEdge(2,3,7)
	graph.addEdge(3,0,10)
	graph.addEdge(3,1,2)
	graph.addEdge(3,2,1)
	graph.addEdge(3,4,6)
	graph.addEdge(4,1,3)
	graph.addEdge(4,2,4)
	graph.addEdge(4,3,9)
	graph.floyd_warshall()
	return graph


def test_floyd_warshall(graph):
	assert graph.showMin(1, 4) == 11
	assert graph.showMin(0, 3) == 16
