# `maths` analysis


## Initial analysis of the maths package
The maths package contains modules that mostly implement a small mathematical function. Most of the tests were manual inspection tests with print statements in main and there were no assertions. These are now moved into a test suite with assertions. While testing, bugs were discovered and fixed. 

## Analysis of tests and fixed bugs

### abs
Existing doctest tests that the function returns the absolute value of a number.

#### Requirements:
**1. Absolute value**  
given a number return its absolute value

#### Coverage
```
Name        Stmts   Miss Branch BrPart  Cover
------------------------------------------------
abs.py       8      1      4      2    75%
```

### absMax
Existing doctest tests that the function returns the number with the biggest absolute value from a list.
#### Requirements:
**1. Smallest absolute value**  
given a list of numbers return the number with the biggest absolute value

#### Coverage
```
Name          Stmts   Miss Branch BrPart  Cover
---------------------------------------------------
absMax.py      12      0      6      1    94%
```

### absMin
Existing doctest tests that the function returns the number with the smallest absolute value from a list.
#### Requirements:
**1. Biggest absolute value**  
given a list of numbers return the number with the smallest absolute value

#### Coverage
```
Name            Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------
abs.py            8      2      4      1    75%
absMin.py        12      0      6      1    94%
-----------------------------------------------------
TOTAL            20      2     10      2    87%
```

### findMin  
Manual inspection print test with one test case.

#### Requirements:

**1. Find smallest number**  
Can find the smallest number in a list of numbers.

#### bugs
Test suite discovers that _findMin_ fails requirement 1 because it used an undefined variable. Fixed by removing the undefined variable and replacing it with the correct value.

#### coverage
```
Name           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------
FindMin.py      10      0      6      1    94%
```
### fibonacci\_sequence\_recursion
Only has a main that takes user input, no automatic coverage or requirements tested. New test suite added a test case instead of taking user input.

#### **Requirements:**

**1. Fibonacci number**  
Can find n:th fibonacci number for any n using recursion

#### bugs
Test suite discovers that _fibonacci\_sequence\_recursion_ fails requirement 1 since the recursive function only returns in the base case. Fixed by adding a return in the recursive call.

## Summary of coverage

### Before
```
Name                                Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
3n+1.py                              17      0      8      2    92%
FindMax.py                           10      0      6      1    94%
FindMin.py                           10      0      6      1    94%
PrimeCheck.py                        11      0      6      1    94%
abs.py                                8      0      4      0   100%
absMax.py                            12      0      6      1    94%
absMin.py                            12      0      6      1    94%
average.py                           12      0      4      1    94%
basic_maths.py                       57      1     28      3    95%
fibonacci_sequence_recursion.py      14      1      8      2    86%
find_hcf.py                          16      2     10      3    81%
find_lcm.py                          14      0      4      1    94%
greater_common_divisor.py            11     11      2      0     0%
modular_exponential.py               15      1      8      2    87%
newton_raphson.py                    30     30     18      0     0%
segmented_sieve.py                   39      1     26      2    95%
sieve_of_eratosthenes.py             22     22     14      0     0%
simpson_rule.py                      32      0      6      1    97%
trapezoidal_rule.py                  29      0      6      1    97%
-------------------------------------------------------------------------
TOTAL                               371     69    176     23    77%
```
### After
```
Name                                Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
FindMax.py                           10      2      6      1    81%
FindMin.py                           10      2      6      1    81%
PrimeCheck.py                        11      4      6      1    71%
abs.py                                8      2      4      1    75%
absMax.py                            12      3      6      1    78%
absMin.py                            12      3      6      1    78%
average.py                           12      2      4      1    81%
basic_maths.py                       57      6     28      3    89%
fibonacci_sequence_recursion.py      14      7      8      1    45%
find_hcf.py                          16      6     10      3    65%
find_lcm.py                          14      4      4      1    72%
greater_common_divisor.py            11      7      2      1    38%
modular_exponential.py               15      3      8      2    78%
newton_raphson.py                    30     11     18      5    58%
segmented_sieve.py                   39      3     26      2    92%
sieve_of_eratosthenes.py             22      3     14      3    83%
simpson_rule.py                      32      7      6      1    79%
three_n_plus_one.py                  17      4      8      2    76%
trapezoidal_rule.py                  29      7      6      1    77%
-------------------------------------------------------------------------
TOTAL                               371     86    176     32    77%
```
--
Note the modules that have 0% are either not tested or take user input