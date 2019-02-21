import os
import re
import importlib
import pytest


def _split_path_rec(path):
    rest, tail = os.path.split(path)
    if rest == "":
        return [tail]
    return _split_path_rec(rest) + [tail]


def _gather_modules():
    """Gather all modules that should be imported."""
    testdir = os.path.dirname(__file__)
    root = os.path.dirname(testdir)
    excludedirs = [os.path.abspath(testdir)]
    modules = []

    for dirpath, dirnames, filenames in os.walk(root, testdir):
        dirnames[:] = [d for d in dirnames if not os.path.abspath(d) in excludedirs]
        for filename in filenames:
            if not filename.endswith(".py"):
                continue
            reldirpath = os.path.relpath(dirpath, testdir)
            path_nodes = _split_path_rec(os.path.join(reldirpath, filename))
            module = ".".join(path_nodes[1:])[:-3]
            modules.append(module)
    return modules


@pytest.mark.parametrize("module", _gather_modules())
@pytest.mark.timeout(0.15) # must be larger than 0.1
def test_import_module(module):
    """Test that all modules from project root can be imported"""
    mod = importlib.import_module(module)
    assert mod
