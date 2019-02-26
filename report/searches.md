# searches

## previously tested requirements
- `binary_search`
  * `binary_search`
    - Finds target in a sorted list that contains it
    - Returns `None` if target is not in a non-empty list
  * `__assert_sorted`
    - Returns `True` if given a non-empty sorted list
    - Raises if given a non-empty unsorted list
- `interpolation_search`
  * `__assert_sorted`
    - Returns `True` if given a non-empty sorted list
    - Raises if given a non-empty unsorted list
- `jump_search`
  * `jump_search`
    - Finds target in a sorted list that contains it
- `linear_search`
  * `linear_search`
    - Finds target in a sorted list that contains it
    - Returns `None` if target is not in a non-empty list
- `sentinel_linear_search`
  * `sentinel_linear_search`
    - Finds target in a sorted list that contains it
    - Returns `None` if target is not in a non-empty list
- `tabu_search`
  * `generate_neighbours`
    - Returns expected neighbor dictionary for non-empty input
  * `generate_first_solution`
    - Returns expected first solution for non-empty input
  * `find_neighbours`
    - Returns the expected neighborhood of solutions for non-empty input
  * `tabu_search`
    - Returns the expected best solution and best cost given complete, non-empty input

Untested modules: `quick_select`, and `ternary_search`.


## fixes

`jump_search` failed tests on travis because it couldn't be run as a main function, and rather had all of its "main" code at the top level.

Refactorored module requirements:
- `jump_search`
  * ID: jump_search_main
  * title: jump_search can be run as a main module
  * description: `jump_search`, when run as a main module, performs a jump search on a hardcoded sorted list that contains the given target. The target value and its index in the hardcoded list is printed. Previously, `jump_search` only did this during import.


## coverage

Coverage before refactor:
```
Name                                 Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------
searches/binary_search.py               50     21     22      1    56%
searches/interpolation_search.py        46     34     22      1    22%
searches/jump_search.py                 22      3     10      3    81%
searches/linear_search.py               19      8     10      1    55%
searches/sentinel_linear_search.py      22     12     10      1    47%
searches/tabu_search.py                110     10     48      4    91%
----------------------------------------------------------------------
TOTAL                                  269     88    122     11    65%
```

Coverage after refactor:
```
Name                                 Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------
searches/binary_search.py               50     13     22      1    75%
searches/interpolation_search.py        46     34     22      1    22%
searches/jump_search.py                 25      4     12      4    78%
searches/linear_search.py               19      8     10      1    55%
searches/sentinel_linear_search.py      22     12     10      1    47%
searches/tabu_search.py                110     10     48      4    91%
----------------------------------------------------------------------
TOTAL                                  272     81    124     12    69%
```
