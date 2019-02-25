# Initial analysis of sorting algorithms
The sorting algorithms are essentially tested in three different ways: with
doctests, with manual print/inspection tests, or not at all. If nothing else is
noted, the tests for any given module all pass.

## bogosort
Existing doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name          Stmts   Miss Branch BrPart  Cover
-----------------------------------------------
bogosort.py      21      7     12      1    70%
```


## bubble_sort
Existing doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers
* Can sort a list with unique numbers
    - Fails because of incorrect formatting (logic is correct)

```
Name             Stmts   Miss Branch BrPart  Cover
--------------------------------------------------
bubble_sort.py      19      7     12      1    68%
```

## bucket_sort
Manual inspection print test with unique numbers only.

```
Name                      Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------
sorts/__init__.py             0      0      0      0   100%
sorts/bucket_sort.py         29      1     18      2    94%
sorts/insertion_sort.py      15      7      8      1    57%
-----------------------------------------------------------
TOTAL                        44      8     26      3    81%
```

## cocktail_shaker_sort
Only has a main that takes user input, no automatic coverage or requirements
tested.

## comb_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name           Stmts   Miss Branch BrPart  Cover
------------------------------------------------
comb_sort.py      23      7     10      1    70%
```

## counting_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name               Stmts   Miss Branch BrPart  Cover
----------------------------------------------------
counting_sort.py      29      9     14      1    67%
```


## cyclesort
Only has a main that takes user input, no automatic coverage or requirements
testsed.

## gnome_sort
Only has a main that takes user input, no automatic coverage or requirements
testsed.

## heap_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name           Stmts   Miss Branch BrPart  Cover
------------------------------------------------
heap_sort.py      28      7     14      1    76%
```

## insertions_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name                Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------
insertion_sort.py      15      7      8      1    57%
```

## merge_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name            Stmts   Miss Branch BrPart  Cover
-------------------------------------------------
merge_sort.py      36      7     14      1    80%
```

## merge_sort_fastest
Nothing.

## pancake_sort
Single manual inspection print test with unique numbers.

```
Name              Stmts   Miss  Cover
-------------------------------------
pancake_sort.py       9      0   100%
```

## quick_sort_3_partition
Only has a main that takes user input, no automatic coverage or requirements
testsed.

## quick_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name            Stmts   Miss Branch BrPart  Cover
-------------------------------------------------
quick_sort.py      17      7     10      1    63%
```

## selection_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name                Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------
selection_sort.py      18      7     10      1    64%
```

## shell_sort
Doctests test the following requirements:

* Can sort an unsorted list with duplicates
* Can sort an empty list
* Can sort a list with negative numbers

```
Name            Stmts   Miss Branch BrPart  Cover
-------------------------------------------------
shell_sort.py      22      7     10      1    69%
```

## timsort
Single manual-inspection print test that sorts unique numbers.

```
Name         Stmts   Miss Branch BrPart  Cover
----------------------------------------------
timsort.py      57      5     32      5    87%
```

## tree_sort
Single manual-inspection print test that sorts unique numbers.

```
Name           Stmts   Miss Branch BrPart  Cover
------------------------------------------------
tree_sort.py      31      2     16      3    89%
```

# Generic testing of sorting algorithms
Most sorting algorithms can be tested in a generic fashion, and this holds true
for all but a few of the algorithms here. All doctests (which are the only
proper test cases in here) attempt to test the same things. We can generalize
what they try to test with requirements 1-3 below. We then add requirements
4-6 ourselves to make the test suite more robust.


## 1
* Title: Sort unsorted list.
* Description: Can sort an unsorted list containing at least some duplicates.

## 2
* Title: Sort empty list.
* Description: Can sort an empty list.

## 3
* Title: Sort list negative numbers.
* Description: Can sort a list with only negative numbers.
* Note: We don't see why this would be important, but we could be wrong so we
  add it in anyway (with a big `LEGACY TEST` note and explanation)

## 4
* Title: Sort reversed list.
* Description: Can sort a reversed list containing at least some duplicates.

## 5
* Title: Sort sorted list.
* Description: Can sort an already sorted list containing at least some
  duplicates.

# 6
* Title: Sort equal elements.
* Description: Can sort a list that contains only duplicates of a single
  element.

## 7
* Title: Out-of-place sorts don't mutate input.
* Description: An out-of-place sorting algorithm should not mutate the input.
  This is of course only applicable to out-of-place sorting algorithms.

## Test files
To make this all happen, we simply added two test files that test in-place
and out-of-place sorts generically using test case parameterization.
[The test files can be found here](TODO: ADD LINK).

## Algorithms that fail our generalized sorting requirements
* `comb_sort`
    - Fails requirement 4
    - Fixed!
* `radix_sort`
    - Fails requirements 1-5 (completely broken)
    - Not fixed, there was no time to debug.
* `merge_sort_fastest`
    - Fails requirement 7
    - Fixed!
* `timsort`
    - Fails requrements 2 and 3
    - Not fixed, there was no time to debug.
* `tree_sort`
    - Fails requirements 1 and 3-6
    - Fixed!
* `bucket_sort`
    - Fails requirement 2
    - Fixed!

# Summary of coverage

## Before

```
Name                      Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------
sorts/__init__.py             0      0      0      0   100%
sorts/bogosort.py            21      7     12      1    70%
sorts/bubble_sort.py         19      7     12      1    68%
sorts/bucket_sort.py         29      1     18      2    94%
sorts/comb_sort.py           23      7     10      1    70%
sorts/counting_sort.py       29      9     14      1    67%
sorts/heap_sort.py           28      7     14      1    76%
sorts/insertion_sort.py      15      7      8      1    57%
sorts/merge_sort.py          36      7     14      1    80%
sorts/pancake_sort.py         9      0      2      0   100%
sorts/quick_sort.py          17      7     10      1    63%
sorts/selection_sort.py      18      7     10      1    64%
sorts/shell_sort.py          22      7     10      1    69%
sorts/timsort.py             57      5     32      5    87%
sorts/tree_sort.py           31      2     16      3    89%
-----------------------------------------------------------
TOTAL                       354     80    182     20    77%
```

## After
```
Name                                            Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------------
sorts/BitonicSort.py                               30     30     14      0     0%
sorts/__init__.py                                   0      0      0      0   100%
sorts/bogosort.py                                  21      7     12      1    70%
sorts/bubble_sort.py                               19      7     12      1    68%
sorts/bucket_sort.py                               29      2     18      1    94%
sorts/cocktail_shaker_sort.py                      23      8     16      1    72%
sorts/comb_sort.py                                 25      7     12      1    73%
sorts/counting_sort.py                             29      9     14      1    67%
sorts/cyclesort.py                                 37     11     24      1    74%
sorts/external-sort.py                            102    102     34      0     0%
sorts/gnome_sort.py                                21      8     12      1    67%
sorts/heap_sort.py                                 28      7     14      1    76%
sorts/insertion_sort.py                            15      7      8      1    57%
sorts/merge_sort.py                                36      7     14      1    80%
sorts/merge_sort_fastest.py                        14      0      2      0   100%
sorts/pancake_sort.py                               9      0      2      0   100%
sorts/quick_sort.py                                17      7     10      1    63%
sorts/quick_sort_3_partition.py                    29      8     12      1    73%
sorts/radix_sort.py                                16      0     10      0   100%
sorts/random_normal_distribution_quicksort.py      46     46      6      0     0%
sorts/selection_sort.py                            18      7     10      1    64%
sorts/shell_sort.py                                22      7     10      1    69%
sorts/timsort.py                                   57      7     32      5    87%
sorts/topological_sort.py                          18     18     10      0     0%
sorts/tree_sort.py                                 33      0     16      1    98%
---------------------------------------------------------------------------------
TOTAL                                             694    312    324     21    58%
```

Note that the files with `0%` coverage were not included in the test-suite as
they were not generic sorting algorithms, and we did not have time to test
them. This skews the `TOTAL` compared to the [Before measurements](#before),
but if you individually inspect the files that previously _had_ coverage, you
will find that they all still have the same amount, or more.
