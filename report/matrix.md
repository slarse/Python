# `matrix` analysis


# Initial analysis of the matrix package
The matrix package contains one module that provides two functions, one for matrix multiplication and one for matrix addition. The test for this module includes creating a pair of small matrices and printing the result of each function called with the matrices in question. No bugs were found for this package.

# Summary of coverage

### Before
```
Name                                Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------
matrix_multiplication_addition.py      30      0     12      1    98%
```
### After
```
Name                                  Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------
matrix_multiplication_addition.py      30      5     12      1    86%
----------------------------------------------------------------------------
TOTAL                                  30      5     12      1    86%
```