# graphs

## Requirements of existing tests

### tarjans\_scc

Contains one assertion testing that:

* The function correctly identifies the strongly connected components of a
  graph with 4 such components

## Summary of coverage

### Before

Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
BFS.py                            16      0      8      1    96%
DFS.py                            15      0      8      1    96%
\_\_init\_\_.py                    0      0      0      0   100%
a\_star.py                        69      2     34      2    96%
articulation\_points.py           38      0     22      1    98%
check\_bipartite\_graph\_bfs.py   29      3     18      4    85%
dijkstra.py                       23      2     12      3    86%
finding\_bridges.py               28      0     14      1    98%
kahns\_algorithm\_long.py         24      0     18      1    98%
kahns\_algorithm\_topo.py         30      2     20      3    90%
multi\_hueristic\_astar.py       197     52    102      7    72%
tarjans\_scc.py                   49      0     26      1    99%
----------------------------------------------------------------
TOTAL                            518     61    282     25    86%

### After

Name                                               Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------------------
BFS.py                                                16      3      8      1    83%
DFS.py                                                15      3      8      1    83%
Directed\_and\_Undirected\_Weighted\_Graph.py        364    364    196      0     0%
\_\_init\_\_.py                                        0      0      0      0   100%
a\_star.py                                            69     69     34      0     0%
articulation\_points.py                               38      3     22      1    93%
basic\_graphs.py                                     154    154    102      0     0%
check\_bipartite\_graph\_bfs.py                       29      6     18      4    79%
dijkstra.py                                           23      6     12      3    74%
finding\_bridges.py                                   28      3     14      1    90%
kahns\_algorithm\_long.py                             24      3     18      1    90%
kahns\_algorithm\_topo.py                             30      7     20      2    78%
minimum\_spanning\_tree\_kruskal.py                   27     27     16      0     0%
minimum\_spanning\_tree\_prims.py                     89     89     38      0     0%
multi\_hueristic\_astar.py                           197    197    102      0     0%
scc\_kosaraju.py                                      38     38     22      0     0%
tarjans\_scc.py                                       49      7     26      1    87%
------------------------------------------------------------------------------------
TOTAL                                               1190    979    656     15    18%
