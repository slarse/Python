# `dynamic_programming` analysis


## Initial analysis of the dynamic_programming package
The dynamic_programming package contains modules that use dynamic programming to solve a well known problem. Most of the tests were manual inspection tests with print statements in main and there were no assertions. These are now moved into a test suite with assertions. While testing, bugs were discovered and fixed. 

## Analysis of tests and fixed bugs
There were no tests that did any assertions. All of them were manual inspection print tests.

### fibonacci
Only has a main that takes user input, no automatic coverage or requirements tested. New test suite added a test case instead of taking user input.

#### Requirements:

**1. Fibonacci sequence**  
Can return a sequence of fibonacci numbers up until a _limit_

#### bugs
Test suite discovers that _fibonacci_ fails requirement 1 since the function does not return the sequence but rather returns a print statement, which is None. Fixed by returning the sequence instead.

## Summary of coverage

### Before
```
Name                                         Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------------
FractionalKnapsack.py                            9      0      4      0   100%
abbreviation.py                                 15      0     14      1    97%
coin_change.py                                  11      0      6      1    94%
edit_distance.py                                42     42     16      0     0%
fastfibonacci.py                                27      6     10      3    76%
fibonacci.py                                    41     41     14      0     0%
floyd_warshall.py                               31     31     12      0     0%
integer_partition.py                            32     32     14      0     0%
k_means_clustering_tensorflow.py                45     45     18      0     0%
knapsack.py                                     23      0     16      1    97%
longest_common_subsequence.py                   23      0     12      1    97%
longest_increasing_subsequence.py               24      0     14      1    97%
longest_increasing_subsequence_O(nlogn).py      24      2     12      2    89%
longest_sub_array.py                            17     11      4      1    33%
matrix_chain_order.py                           31      0     16      1    98%
max_sub_array.py                                47     47     22      0     0%
minimum_partition.py                            18     18     16      0     0%
rod_cutting.py                                  20      1     14      1    94%
------------------------------------------------------------------------------
TOTAL                                          480    276    234     13    44%
```
### After
```
Name                                        Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------------------------------
FractionalKnapsack.py                         9      0      4      0   100%
abbreviation.py                              15      1     14      1    93%
coin_change.py                               11      2      6      1    82%
edit_distance.py                             42     17     16      3    66%
fastfibonacci.py                             27     10     10      1    65%
fibonacci.py                                 41     26     14      4    38%
floyd_warshall.py                            31     15     12      1    63%
integer_partition.py                         32     12     14      1    67%
k_means_clustering_tensorflow.py             45     45     18      0     0%
knapsack.py                                  23     13     16      1    49%
longest_common_subsequence.py                23      3     12      1    89%
longest_increasing_subsequence.py            27      3     16      2    88%
longest_increasing_subsequence_nlogn.py      24      2     12      2    89%
longest_sub_array.py                         17      4      4      1    76%
matrix_chain_order.py                        31     12     16      2    66%
max_sub_array.py                             47     47     22      0     0%
minimum_partition.py                         18      0     16      2    94%
rod_cutting.py                               20      1     14      1    94%
-----------------------------------------------------------------------------------------------
TOTAL                                       483    213    236     24    59%
```

--

Note the modules that have 0% are either not tested or take user input