from data_structures.graph.dijkstra import Dijkstra

def test_dijkstra():
    '''Testing dijkstra with a graph containing 4 edges and 4 vertices'''
    V = 4
    E = 4
    
    graph = [[float('inf') for i in range(V)] for j in range(V)]
    
    for i in range(V):
        graph[i][i] = 0.0
    
    for i in range(E):
        src = i
        dst = E -1
        weight = 1
        graph[src][dst] = weight
    
    
    gsrc = 1
    
    assert Dijkstra(graph, V, gsrc) == [float('inf'), 0.0, float('inf'), 1.0]
