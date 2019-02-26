# arithmetic_analysis

The file `newton_raphson_method.py` crashed when its main method runs because
the function `NewtonRaphson` is broken. We found that it would require too
much effort to fix this. The coverage shows how much of the code is executed
before it crashes.

## Summary of coverage

### Before

```
Name                       Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------
__init__.py                0      0      0      0   100%
bisection.py                  26      5     14      5    75%
intersection.py               16      0      4      1    95%
lu_decomposition.py          27      2     14      3    88%
newton_method.py             15      0      4      1    95%
newton_raphson_method.py    15      6      4      1    53%
------------------------------------------------------------
TOTAL                         99     13     40     11    81%
```

### After

```
Name                                           Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------
__init__.py                                    0      0      0      0   100%
bisection.py                                      26      7     14      5    70%
intersection.py                                   16      2      4      1    85%
lu_decomposition.py                              27      7     14      3    76%
newton_method.py                                 15      2      4      1    84%
newton_raphson_method.py                        15      8      4      1    42%
--------------------------------------------------------------------------------
TOTAL                                             99     26     40     11    72%
```

# binary_tree

## Summary of coverage

### Before

```
Name                   Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------
__init__.py            0      0      0      0   100%
basic_binary_tree.py    35      1     12      2    94%
--------------------------------------------------------
TOTAL                     35      1     12      2    94%
```

### After

```
Name                               Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------
__init__.py                        0      0      0      0   100%
basic_binary_tree.py                35     13     12      2    68%
--------------------------------------------------------------------
TOTAL                                 35     13     12      2    68%
```

# graphs

## Requirements of existing tests

### tarjans_scc

Contains one assertion testing that:

* The function correctly identifies the strongly connected components of a
  graph with 4 such components

## Summary of coverage

### Before

```
Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
BFS.py                            16      0      8      1    96%
DFS.py                            15      0      8      1    96%
__init__.py                    0      0      0      0   100%
a_star.py                        69      2     34      2    96%
articulation_points.py           38      0     22      1    98%
check_bipartite_graph_bfs.py   29      3     18      4    85%
dijkstra.py                       23      2     12      3    86%
finding_bridges.py               28      0     14      1    98%
kahns_algorithm_long.py         24      0     18      1    98%
kahns_algorithm_topo.py         30      2     20      3    90%
multi_hueristic_astar.py       197     52    102      7    72%
tarjans_scc.py                   49      0     26      1    99%
----------------------------------------------------------------
TOTAL                            518     61    282     25    86%
```

### After

```
Name                                               Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------------------
BFS.py                                                16      3      8      1    83%
DFS.py                                                15      3      8      1    83%
Directed_and_Undirected_Weighted_Graph.py        364    364    196      0     0%
__init__.py                                        0      0      0      0   100%
a_star.py                                            69     69     34      0     0%
articulation_points.py                               38      3     22      1    93%
basic_graphs.py                                     154    154    102      0     0%
check_bipartite_graph_bfs.py                       29      6     18      4    79%
dijkstra.py                                           23      6     12      3    74%
finding_bridges.py                                   28      3     14      1    90%
kahns_algorithm_long.py                             24      3     18      1    90%
kahns_algorithm_topo.py                             30      7     20      2    78%
minimum_spanning_tree_kruskal.py                   27     27     16      0     0%
minimum_spanning_tree_prims.py                     89     89     38      0     0%
multi_hueristic_astar.py                           197    197    102      0     0%
scc_kosaraju.py                                      38     38     22      0     0%
tarjans_scc.py                                       49      7     26      1    87%
------------------------------------------------------------------------------------
TOTAL                                               1190    979    656     15    18%
```

# hashes

## Requirements of existing tests

### md5

Contains two assertions which test that:

* The function produces the correct hash given an empty string
* The function produces the correct hash given the string "The quick brown fox
  jumps over the lazy dog"

### sha1

Contains one proper unit test testing that:

* The function produces the same hash as the standard library sha1 function
  given the string "Test string"

## Summary of coverage

### Before

```
Name               Stmts   Miss Branch BrPart  Cover
----------------------------------------------------
__init__.py        0      0      0      0   100%
chaos_machine.py     50     18     10      2    63%
md5.py                87      1     30      2    97%
sha1.py               60      4     20      3    91%
----------------------------------------------------
TOTAL                197     23     60      7    88%
```

### After

```
Name                      Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------
__init__.py               0      0      0      0   100%
chaos_machine.py            50     50     10      0     0%
md5.py                       87      5     30      2    94%
sha1.py                      56     11     20      2    80%
-----------------------------------------------------------
TOTAL                       193     66     60      4    68%
```

# other

## Requirements of existing tests

### detecting_english_programmatically

Contains two doctests testing the following requirements:

* Can identify string belonging to the English language
* Can identify string not belonging to the English language

### frequency_finder

Contains one doctest testing that:

* The frequency score of the string "Hello World" is 1

### tower_of_hanoi

Contains one doctest testing that:

* The optimal sequence of moves are chosen given a tower of height 3

## Summary of coverage

### Before

```
Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
__init__.py                             0      0      0      0   100%
anagrams.py                                23      0      8      0   100%
binary_exponentiation.py                  17     14      8      0    12%
binary_exponentiation_2.py               17     14      8      0    12%
detecting_english_programmatically.py    39      1     14      2    94%
euclidean_gcd.py                          15      0      4      0   100%
findingPrimes.py                           12      9     12      0    12%
fischer_yates_shuffle.py                 16      0      4      0   100%
frequency_finder.py                       42      1     22      1    97%
linear_congruential_generator.py         18     10      2      1    45%
nested_brackets.py                        20     16     12      1    16%
palindrome.py                              21      2     10      2    87%
password_generator.py                     24      4     10      0    88%
primelib.py                               190    171     74      0     7%
sierpinski_triangle.py                    28     21      6      1    24%
tower_of_hanoi.py                        13      3      4      1    76%
two_sum.py                                11      9      4      0    13%
word_patterns.py                          29      0     10      0   100%
-------------------------------------------------------------------------
TOTAL                                     535    275    212      9    46%
```

### After

```
Name                                          Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------
__init__.py                                   0      0      0      0   100%
anagrams.py                                      23     23      8      0     0%
binary_exponentiation.py                        17     17      8      0     0%
binary_exponentiation_2.py                     17     17      8      0     0%
detecting_english_programmatically.py          39      3     14      3    89%
euclidean_gcd.py                                15      6      4      1    63%
findingPrimes.py                                 12     12     12      0     0%
fischer_yates_shuffle.py                       16      6      4      1    65%
frequency_finder.py                             42      3     22      2    92%
game_of_life/__init__.py                    0      0      0      0   100%
game_of_life/game_o_life.py                  59     59     30      0     0%
linear_congruential_generator.py               18      4      2      1    75%
nested_brackets.py                              20     20     12      0     0%
palindrome.py                                    21      6     10      3    71%
password_generator.py                           24     24     10      0     0%
primelib.py                                     190    190     74      0     0%
sierpinski_triangle.py                          28     28      6      0     0%
tower_of_hanoi.py                              13      3      4      1    76%
two_sum.py                                      11     11      4      0     0%
word_patterns.py                                29     29     10      0     0%
-------------------------------------------------------------------------------
TOTAL                                           594    461    242     12    22%
```
