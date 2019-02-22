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

Did it build as documented?
    
(See the assignment for details; if everything works out of the box,
there is no need to write much here.)

## Requirements affected by functionality being refactored

## Existing test cases relating to refactored code

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
