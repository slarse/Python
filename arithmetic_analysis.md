# arithmetic\_analysis

The file `newton_raphson_method.py` crashed when its main method runs because
the function `NewtonRaphson` is broken. We found that it would require too
much effort to fix this. The coverage shows how much of the code is executed
before it crashes.

## Summary of coverage

### Before

Name                       Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------
\_\_init\_\_.py                0      0      0      0   100%
bisection.py                  26      5     14      5    75%
intersection.py               16      0      4      1    95%
lu\_decomposition.py          27      2     14      3    88%
newton\_method.py             15      0      4      1    95%
newton\_raphson\_method.py    15      6      4      1    53%
------------------------------------------------------------
TOTAL                         99     13     40     11    81%

### After

Name                                           Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------
\_\_init\_\_.py                                    0      0      0      0   100%
bisection.py                                      26      7     14      5    70%
intersection.py                                   16      2      4      1    85%
lu\_decomposition.py                              27      7     14      3    76%
newton\_method.py                                 15      2      4      1    84%
newton\_raphson\_method.py                        15      8      4      1    42%
--------------------------------------------------------------------------------
TOTAL                                             99     26     40     11    72%
