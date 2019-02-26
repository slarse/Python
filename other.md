# other

## Requirements of existing tests

### detecting\_english\_programmatically

Contains two doctests testing the following requirements:

* Can identify string belonging to the English language
* Can identify string not belonging to the English language

### frequency\_finder

Contains one doctest testing that:

* The frequency score of the string "Hello World" is 1

### tower\_of\_hanoi

Contains one doctest testing that:

* The optimal sequence of moves are chosen given a tower of height 3

## Summary of coverage

### Before

Name                                    Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------
\_\_init\_\_.py                             0      0      0      0   100%
anagrams.py                                23      0      8      0   100%
binary\_exponentiation.py                  17     14      8      0    12%
binary\_exponentiation\_2.py               17     14      8      0    12%
detecting\_english\_programmatically.py    39      1     14      2    94%
euclidean\_gcd.py                          15      0      4      0   100%
findingPrimes.py                           12      9     12      0    12%
fischer\_yates\_shuffle.py                 16      0      4      0   100%
frequency\_finder.py                       42      1     22      1    97%
linear\_congruential\_generator.py         18     10      2      1    45%
nested\_brackets.py                        20     16     12      1    16%
palindrome.py                              21      2     10      2    87%
password\_generator.py                     24      4     10      0    88%
primelib.py                               190    171     74      0     7%
sierpinski\_triangle.py                    28     21      6      1    24%
tower\_of\_hanoi.py                        13      3      4      1    76%
two\_sum.py                                11      9      4      0    13%
word\_patterns.py                          29      0     10      0   100%
-------------------------------------------------------------------------
TOTAL                                     535    275    212      9    46%

### After

Name                                          Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------
\_\_init\_\_.py                                   0      0      0      0   100%
anagrams.py                                      23     23      8      0     0%
binary\_exponentiation.py                        17     17      8      0     0%
binary\_exponentiation\_2.py                     17     17      8      0     0%
detecting\_english\_programmatically.py          39      3     14      3    89%
euclidean\_gcd.py                                15      6      4      1    63%
findingPrimes.py                                 12     12     12      0     0%
fischer\_yates\_shuffle.py                       16      6      4      1    65%
frequency\_finder.py                             42      3     22      2    92%
game\_of\_life/\_\_init\_\_.py                    0      0      0      0   100%
game\_of\_life/game\_o\_life.py                  59     59     30      0     0%
linear\_congruential\_generator.py               18      4      2      1    75%
nested\_brackets.py                              20     20     12      0     0%
palindrome.py                                    21      6     10      3    71%
password\_generator.py                           24     24     10      0     0%
primelib.py                                     190    190     74      0     0%
sierpinski\_triangle.py                          28     28      6      0     0%
tower\_of\_hanoi.py                              13      3      4      1    76%
two\_sum.py                                      11     11      4      0     0%
word\_patterns.py                                29     29     10      0     0%
-------------------------------------------------------------------------------
TOTAL                                           594    461    242     12    22%
