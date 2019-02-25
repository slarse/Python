from data_structures.graph.bellman_ford import BellmanFord

class TestBellmanFord:
    
    def test_bellman_ford(self):
        V = 4
        E = 4
    
        graph = [dict() for j in range(E)]
    
        for i in range(V):
            graph[i][i] = 0.0
    
        for i in range(E):
            src = i
            dst = E-1
            weight = 1
            graph[i] = {"src": src,"dst": dst, "weight": weight}
    
    
        gsrc = 1
    
        assert BellmanFord(graph, V, E, gsrc) == [float('inf'), 0.0, float('inf'), 1.0]
