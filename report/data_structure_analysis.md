# Initial analysis of data_structures
All data structures are essentially tested in three different ways: with
unittest, with manual print/inspection tests, or not at all. If nothing else is
noted, the tests for any given module all pass.

## trie
Existing test cases test the following requirement:

* Working of find()
* Testing whether a node is existing in Tree or not

```
Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
data_structures/trie/trie.py      36      4     16      1    83%
```


## union_find
Existing unittest test the following requirements:

* Check the validity of size parameter of the set
* Check whether set contains valid values 
* Check whether the same set contains valid values or not

```
Name                                             Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------------
data_structures/union_find/tests_union_find.py      56      0     12      1    99%
data_structures/union_find/union_find.py            33      1     16      1    96%
----------------------------------------------------------------------------------
TOTAL                                               89      1     28      2    97%
```

## binary_tree.AVLtree
Manual inspection print test which creates a tree,add nodes and delete nodes

```
Name                                     Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------
data_structures/binary_tree/AVLtree.py     202     28     64     10    83%
```

## binary_tree.binary_search_tree
Manual testing with print statements, checking creation of tree, adding nodes, deleting nodes and searching nodes in tree
```
Name                                                Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------------
data_structures/binary_tree/binary_search_tree.py     153      4     64     12    93%
```

## binary_tree.fenwick_tree
Manual testing with print statements, checking create, update and query methods in a tree
```
Name                                          Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------
data_structures/binary_tree/fenwick_tree.py      25      0      8      1    97%
```
## binary_tree.lazy_segment_tree
Manual testing with print statements, checking building, updating and querying a lazy segment tree
```
Name                                               Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------------------
data_structures/binary_tree/lazy_segment_tree.py      77     11     30      3    85%
```
## binary_tree.segment_tree
Manual testing with print statements, testing querying and updating methods of a tree
```
Name                                          Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------
data_structures/binary_tree/segment_tree.py      58      0     14      1    99%
```
## graph.bellman_ford
Only has a main that takes user input, no automatic coverage or requirements tested.

## graph.breadth_first_search
Manual testing with print statements, checking adding of a edge, searching for a node in graph
```
Name                                            Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------------
data_structures/graph/breadth_first_search.py      35      0     14      1    98%
``` 
## graph.depth_first_search
Manual testing with print statements, checking adding of a edge, searching for a node in graph
```
Name                                          Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------
data_structures/graph/depth_first_search.py      35      0     16      1    98%
```
## graph.dijkstra
Only has a main that takes user input, no automatic coverage or requirements tested.

## graph.dijkstra_algorithm
Manual testing with print statements, checking for finding the shortest path for a mentioned node
```
Name                                          Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------
data_structures/graph/dijkstra_algorithm.py     130      4     44      6    94%
```
## graph.floyd_warshall
Only has a main that takes user input, no automatic coverage or requirements tested.

## graph.graph
Manual testing with print statements, converting the graph into a adjacency list
```
Name                             Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------
data_structures/graph/graph.py      24      0      8      1    97%
```
## graph.graph_list
Manual testing with print statements, converting the graph into a list
```
Name                                  Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------
data_structures/graph/graph_list.py      21      0      8      1    97%
```
## graph.graph_matrix
Manual testing with print statements, converting the graph into a matrix
```
Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
data_structures/graph/graph_matrix.py      21      0      8      1    97%
```
## heap
Only has a main that takes user input, no automatic coverage or requirements tested.
## stacks.balanced_parentheses
Manual testing with print statements, checking if parentheses are balanced or not
```
Name                                             Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------------
data_structures/stacks/balanced_parentheses.py      19      0     12      2    94%
data_structures/stacks/stack.py                     40     19     10      3    48%
----------------------------------------------------------------------------------
TOTAL                                               59     19     22      5    65%
```
##  stacks.infix_to_postfix_conversion
Manual testing with print statements, checking conversion of infix to postfix expression
```
Name                                                    Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------------------------
data_structures/stacks/infix_to_postfix_conversion.py      36      1     20      3    93%
data_structures/stacks/stack.py                            40     17     10      4    54%
-----------------------------------------------------------------------------------------
TOTAL                                                      76     18     30      7    75%
```
## stacks.stack
Manual testing using print statements, testing create, pop, push, display methods on a stack
```
Name                              Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------
data_structures/stacks/stack.py      40      3     10      4    86%
```
##  stacks.stock_span_problem
Manual testing using print statements, testing the method to solve stock span problem 
```
Name                                           Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------
data_structures/stacks/stock_span_problem.py      18      0      8      0   100%
```

# Requirements tested in data_structures

1. Add new element to data structure
2. Delete an existing element from data structure
3. Query an existing element in data structure
4. Able to implement algorithms on top of those data structures

## Test files
To make this all happen, we simply added test files
[The test files can be found here](TODO: ADD LINK).

## Data structures that fail
* `graph.even_tree`
    - Broken
* `hashing`
    - No test modules available 
* `queue`
    - No test modules available
* `linked_list`
    - No test modules available
* `graph.bellman_ford`
    - Only prints the output, no test modules available
    - Fixed!
* `graph.dijkstra`
    - Only prints the output, no test modules available
    - Fixed!
 * `graph.floyd_warshall`
	- Only prints the output, no test modules available
    - Fixed!
 * `heap`
	- Only prints the output, no test modules available
    - Fixed!

# Summary of coverage

## Before

```
Name                                                Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------------
data_structures/binary tree/AVLtree.py                201     26     64     10    85%
data_structures/binary tree/binary_search_tree.py     153      4     64     12    93%
data_structures/binary tree/fenwick_tree.py            25      0      8      1    97%
data_structures/binary tree/lazy_segment_tree.py       77     11     30      3    85%
data_structures/binary tree/segment_tree.py            58      0     14      1    99%
-------------------------------------------------------------------------------------
TOTAL                                                 514     41    180     27    89%

Name                                            Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------------
data_structures/graph/bellman_ford.py              39      2     22      1    95%
data_structures/graph/breadth_first_search.py      35      0     14      1    98%
data_structures/graph/depth_first_search.py        35      0     16      1    98%
data_structures/graph/dijkstra.py                  40      0     24      0   100%
data_structures/graph/dijkstra_algorithm.py       130      4     44      6    94%
data_structures/graph/even_tree.py                 25      0     10      1    97%
data_structures/graph/floyd_warshall.py            32      1     26      1    97%
data_structures/graph/graph.py                     24      0      8      1    97%
data_structures/graph/graph_list.py                20      0      6      0   100%
data_structures/graph/graph_matrix.py              20      0      6      0   100%
---------------------------------------------------------------------------------
TOTAL                                             400      7    176     12    97%


Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
data_structures/trie/trie.py      35      4     14      0    84%

Name                                       Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------
data_structures/union_find/union_find.py      33     27     16      0    12%

Name                                                    Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------------------------
data_structures/stacks/balanced_parentheses.py             19      0     12      2    94%
data_structures/stacks/infix_to_postfix_conversion.py      36     32     20      0     7%
data_structures/stacks/stack.py                            40      3     10      3    88%
data_structures/stacks/stock_span_problem.py               18      0      8      0   100%
-----------------------------------------------------------------------------------------
TOTAL                                                     113     35     50      5    63%

```

## After
```
Name                                                           Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------------------------------
data_structures/__init__.py                                        0      0      0      0   100%
data_structures/binary_tree/AVLtree.py                           198    160     64      1    15%
data_structures/binary_tree/__init__.py                            0      0      0      0   100%
data_structures/binary_tree/binary_search_tree.py                121     95     54      0    15%
data_structures/binary_tree/fenwick_tree.py                       25     19      8      1    21%
data_structures/binary_tree/lazy_segment_tree.py                  77     66     30      1    11%
data_structures/binary_tree/segment_tree.py                       59     46     14      1    19%
tests/data_structures/binary_tree/test_AVLtree.py                 24     20      6      0    13%
tests/data_structures/binary_tree/test_binary_search_tree.py      52     46      4      0    11%
tests/data_structures/binary_tree/test_fenwick_tree.py            15     12      0      0    20%
tests/data_structures/binary_tree/test_lazy_segment_tree.py       26     21      0      0    19%
tests/data_structures/binary_tree/test_segment_tree.py            12      9      0      0    25%
------------------------------------------------------------------------------------------------
TOTAL                                                            609    494    180      4    15%

Name                                                       Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------------------
data_structures/__init__.py                                    0      0      0      0   100%
data_structures/graph/__init__.py                              0      0      0      0   100%
data_structures/graph/bellman_ford.py                         41     37     24      1     8%
data_structures/graph/breadth_first_search.py                 35     27     14      1    18%
data_structures/graph/depth_first_search.py                   35     26     16      1    20%
data_structures/graph/dijkstra.py                             42     37     26      1     9%
data_structures/graph/dijkstra_algorithm.py                  131    109     44      1    13%
data_structures/graph/floyd_warshall.py                       34     30     28      1     8%
data_structures/graph/graph.py                                24     18      8      1    22%
data_structures/graph/graph_list.py                           21     15      8      1    24%
data_structures/graph/graph_matrix.py                         21     15      8      1    24%
tests/data_structures/graph/test_bellman_ford.py              14     12      6      0    10%
tests/data_structures/graph/test_breadth_first_search.py      13     11      2      0    13%
tests/data_structures/graph/test_depth_first_search.py        13     11      2      0    13%
tests/data_structures/graph/test_dijkstra.py                  14     12      6      0    10%
tests/data_structures/graph/test_dijkstra_algorithm.py        19     17      0      0    11%
tests/data_structures/graph/test_floyd_warshall.py            14     12      6      0    10%
tests/data_structures/graph/test_graph.py                     14     12      0      0    14%
tests/data_structures/graph/test_graph_list.py                11      9      2      0    15%
tests/data_structures/graph/test_graph_matrix.py               9      7      0      0    22%
--------------------------------------------------------------------------------------------
TOTAL                                                        505    417    200      9    14%

Name                                      Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------
data_structures/__init__.py                   0      0      0      0   100%
data_structures/heap/__init__.py              0      0      0      0   100%
data_structures/heap/heap.py                 74     57     22      1    19%
tests/data_structures/heap/test_heap.py       7      5      0      0    29%
---------------------------------------------------------------------------
TOTAL                                        81     62     22      1    19%

Name                                      Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------
data_structures/__init__.py                   0      0      0      0   100%
data_structures/trie/__init__.py              0      0      0      0   100%
data_structures/trie/trie.py                 26     20     14      0    15%
tests/data_structures/trie/test_trie.py      13     10      0      0    23%
---------------------------------------------------------------------------
TOTAL                                        39     30     14      0    17%

Name                                       Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------
data_structures/__init__.py                    0      0      0      0   100%
data_structures/union_find/__init__.py         0      0      0      0   100%
data_structures/union_find/union_find.py      33     27     16      0    12%
----------------------------------------------------------------------------
TOTAL                                         33     27     16      0    12%

Name                                                               Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------------------------------
data_structures/__init__.py                                            0      0      0      0   100%
data_structures/stacks/__init__.py                                     0      0      0      0   100%
data_structures/stacks/balanced_parentheses.py                        19     13     12      1    23%
data_structures/stacks/infix_to_postfix_conversion.py                 36     27     20      1    18%
data_structures/stacks/stack.py                                       40     26     10      1    30%
data_structures/stacks/stock_span_problem.py                          21     16     10      1    19%
tests/data_structures/stacks/test_balanced_parentheses.py             10      6      0      0    40%
tests/data_structures/stacks/test_infix_to_postfix_conversion.py       4      2      0      0    50%
tests/data_structures/stacks/test_stack.py                            28     22     10      0    16%
tests/data_structures/stacks/test_stock_span_problem.py                6      4      2      0    25%
----------------------------------------------------------------------------------------------------
TOTAL                                                                164    116     64      4    23%
```
