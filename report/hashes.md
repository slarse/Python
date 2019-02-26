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
__init__.py            0      0      0      0   100%
chaos_machine.py      50     18     10      2    63%
md5.py                87      1     30      2    97%
sha1.py               60      4     20      3    91%
----------------------------------------------------
TOTAL                197     23     60      7    88%
```

### After

```
Name                      Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------
__init__.py                   0      0      0      0   100%
chaos_machine.py             50     50     10      0     0%
md5.py                       87      5     30      2    94%
sha1.py                      56     11     20      2    80%
-----------------------------------------------------------
TOTAL                       193     66     60      4    68%
```
