# Report for assignment 4

## Project

Name: TheAlgorithms/Python

URL: [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)

A collection of common algorithms implemented in Python for educational purposes.


## Selected issue(s)

Title: Adopt a more robust testing system \#309

URL: [#309](https://github.com/TheAlgorithms/Python/issues/309)

The current tests are incoherent and very limited in capability. There are few tests with each algorithm. Refactor into a more robust testing system.

## Onboarding experience

Onboarding is a bit of a mixed bag, probably much due to the lack of a
coherent test suite that can test the whole project. The project is internally
structured more like a collection of projects, than a single library. As
explained in [Test logs](#test-logs), certain parts support Python 2, others
Python 3, and some parts are seemingly just not working as intended. When it
comes to Python 3, most modules run just fine as long as you have a somewhat
recent version of Python 3 (~3.5+). This is the apex of onboarding: there is
none whatsoever, it just works out of the box. However, many of the more
advanced parts of the library, such as the `machine_learning` modules, rely on
external dependencies that are often not listed anywhere. You notice simply by
the fact that importing the module fails as some dependencies cannot be
resolved. Preferably, dependencies should be listed of a `setup.py` file such
that the project can be installed as a package, with dependencies.  We also
found that certain parts rely on
[`Tcl/Tk`](https://www.tcl.tk/software/tcltk/), which must be installed
separately. This is also not specified anywhere. Despite the somewhat convoluted
onboarding experience, we chose to proceed with refactoring this project mostly
because we thought we could do some real good here.

## Requirements affected by functionality being refactored

## Existing test cases relating to refactored code

* [arithmetic_analysis](./arithmetic_analysis.md)
* [binary_tree](./binary_tree.md)
* [graphs](./graphs.md)
* [hashes](./hashes.md)
* [other](./other.md)

## The refactoring carried out

(Link to) a UML diagram and its description

## Test logs

Before we started our refactoring, the repository did contain a few proper unit
tests, but many were simply print statements. Before we started modifying the
code, we set up a `pytest` test suite and added a test to see how many modules
could be imported without errors in Python 2 and Python 3. The results were as
follows:

* [Python 2](before/py2_cov)
  - 150 tests passed
  - 106 tests failed
    - 14 IOErrors
    - 4 timeouts
    - 81 ImportErrors
  - 20 % code coverage
* [Python 3](before/py3_cov)
  - 171 tests passed
  - 85 tests failed
    - 32 OSErrors
    - 11 timeouts
    - 33 ModuleNotFoundErrors
  - 22 % code coverage

## Effort spent

For each team member, how much time was spent in

1. plenary discussions/meetings;

2. discussions within parts of the group;

3. reading documentation;

4. configuration;

5. analyzing code/output;

6. writing documentation;

7. writing code;

8. running code?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
