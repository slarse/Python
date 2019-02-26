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

* [data_structures_analysis](./data_structure_analysis.md)
* [strings_analysis](./strings_analysis.md)

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

After our refactoring, all modules can be imported in Python 3. We decided to
drop support for Python 2 due to lack of time. In the test logs produced after
our refactoring, we also decided to not add a `thealgorithms` top-level
directory. The test logs can be found [here](after/py3_cov). The code coverage
including our new tests is 46 %.

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

In the assignment description, the goal of this assignment is to teach us "the complexity of refactoring in a real project." This sentence sums up the main takeaway lesson well, and, in that sense, this assignment was a success. In particular, what we planned to do turned out to involve a whole lot more unexpected work. And in the end, it was the unexpected work that took the most time.

As with the last assignment, the corollary takeaway is that even popular repos can be slipshod and difficult to maintain. Our chosen repo this time is a very extreme example, however. This repo is extremely difficult to maintain. The repo is not a package, but rather a broad collection of algorithms and solutions for education or demonstration purposes. It is expected, then, for the contents to be at least inconsistent. The problem, however, is that the solutions are mostly untested, or at least tested in an idiosyncratic manner. Consequently, in constructing a centralized testing suite for the repo, we ended up on some level standardizing the entire project.

Note that although one of the most starred python repos on Github, and although comprising about 250 modules, our chosen repo has only about a couple maintainers. As our work revealed, several to most of the modules don't run in any useful way or are downright broken. Unfortunately, we do not have time to fix them all. So, another main takeaway is just how important robust and automated testing really is for the long term.

Another takeaway that somewhat mirrors the last assignment is some frustration with the assignment. While more clear and centralized in its tasks compared to the previous assignment, this assignment nevertheless has some problems.

It seems to us that either the time frame needs to be extended or the project selection requirements need to be relaxed. Probably both. It is incredibly difficult to find a project that satisfies the requirements, that has an already open refactor issue that is not being worked on, and, on top of all that, that can be gotten into quickly. It was said that it is OK to choose a smaller project, but 10k lines seems far from small, especially for the more concise languages. We consider ourselves very lucky in finding a relatively manageable project. For at least the past week, however, many of us have had to treat this course as if it were a full time job.
