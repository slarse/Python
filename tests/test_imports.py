import os
import re
import importlib


def _split_path_rec(path):
    rest, tail = os.path.split(path)
    if rest == '':
        return [tail]
    return _split_path_rec(rest) + [tail]
    

def test_all_modules_can_be_imported():
    """test that all modules from project root can be imported"""
    testdir = os.path.dirname(__file__)
    root = os.path.dirname(testdir)
    excludedirs = [os.path.abspath(testdir)]
    
    for dirpath, dirnames, filenames in os.walk(root, testdir):
        dirnames[:] = [d for d in dirnames if not os.path.abspath(d) in excludedirs]
        for filename in filenames:
            if not filename.endswith(".py"):
                continue
            reldirpath = os.path.relpath(dirpath, testdir)
            path_nodes = _split_path_rec(os.path.join(reldirpath, filename))
            s = ".".join(path_nodes[1:])[:-3]
            importlib.import_module(s)
