#! /bin/bash
#
# Script for running the test suite.
# Requires bash>=3.2

# Coverage.py caches interfere with subsequent runs for some reason
rm -f .coverage*

python -m pytest tests/ $(python .travis/covstring.py) --cov-branch
