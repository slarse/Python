# Initial analysis of strings
All strings implementation are essentially tested in three different ways: with unittest, with manual print/inspection tests, or not at all. If nothing else is noted, the tests for any given module all pass.

## knuth_morris_pratt
Existing test cases test the following requirement:
* Pattern matching, return true if pattern found in a string

```
Name                            Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------
strings/knuth_morris_pratt.py      42      0     16      1    98%
```


## levenshtein_distance
Only has a main that takes user input, no automatic coverage or requirements tested.

## manacher
Only has a main that takes user input, no automatic coverage or requirements tested.

## min_cost_string_conversion
Manual testing with print statements, calculating cost for converting/replacing  a string value with another 
```
Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
strings/min_cost_string_conversion.py      84      8     34      3    91%
```

## rabin_karp
Existing test cases test the following requirement:
* Pattern matching, return true if pattern found in a string

```
Name                    Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------
strings/rabin_karp.py      22      0      6      1    96%
```
# Requirements tested in strings
Each file in string package has different purpose and are tested differently, `knuth_moris_pratt` and `rabin_karp` are tested for pattern matching. `levenshtein_distance`  tested for calculating distance between two string values. `min_cost_string_conversion`  tested for calculating cost for replacing a string with another. `manacher` is tested for finding a palindromic string in a string

## Test files
To make this all happen, we simply added test files
[The test files can be found here](TODO: ADD LINK).

## Strings that fail
* `levenhstein_distance`
    - No test modules available
    - Fixed
* `manacher`
    - No test modules available 
    - Fixed
* `min_cost_string_conversion`
    - Only prints the output, not test modules available
    - Fixed
 
# Summary of coverage

## Before

```
Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
strings/knuth_morris_pratt.py              42      0     16      1    98%
strings/levenshtein_distance.py            24      2     10      3    85%
strings/manacher.py                        23      0     14      1    97%
strings/min_cost_string_conversion.py      84      8     34      3    91%
strings/rabin_karp.py                      22      0      6      1    96%
-------------------------------------------------------------------------
TOTAL                                     195     10     80      9    93%
```

## After
```
Name                                               Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------------------
strings/__init__.py                                    0      0      0      0   100%
strings/knuth_morris_pratt.py                         26     24     14      0     5%
strings/levenshtein_distance.py                       24     22     10      1     9%
strings/manacher.py                                   23     20     14      1    11%
strings/min_cost_string_conversion.py                 89     79     34      1     9%
strings/rabin_karp.py                                  8      7      4      0     8%
tests/strings/test_knuth_morris_pratt.py              21     15      0      0    29%
tests/strings/test_levenshtein_distance.py            11      8      0      0    27%
tests/strings/test_manacher.py                         8      5      0      0    38%
tests/strings/test_min_cost_string_conversion.py       8      6      0      0    25%
tests/strings/test_rabin_karp.py                      18     13      0      0    28%
------------------------------------------------------------------------------------
TOTAL                                                236    199     76      3    13%
```
