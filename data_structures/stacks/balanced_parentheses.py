from __future__ import print_function
from __future__ import absolute_import
from .stack import Stack

__author__ = 'Omkar Pathak'


def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses is balanced."""
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
