from data_structures.graph.floyd_warshall import FloydWarshall

class TestFloydWarshall:
    
    def test_floyd_warshall(self):
        V = 4
        E = 4
    
        graph = [[float('inf') for i in range(V)] for j in range(V)]
    
        for i in range(V):
            graph[i][i] = 0.0
    
        for i in range(E):
            print("\nEdge ",i+1)
            src = i
            dst = E-1
            weight = 1
            graph[src][dst] = weight
    
        assert FloydWarshall(graph, V) == [[0.0, float('inf'), float('inf'), 1.0], [float('inf'), 0.0, float('inf'), 1.0], [float('inf'), float('inf'), 0.0, 1.0], [float('inf'), float('inf'), float('inf'), 1.0]]
