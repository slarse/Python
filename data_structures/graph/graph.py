#!/usr/bin/python


from __future__ import print_function
# Author: OMKAR PATHAK

# We can use Python's dictionary for constructing the graph

class AdjacencyList(object):
    def __init__(self):
        self.List = {}

    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        for i  in self.List:
            print((i,'->',' -> '.join([str(j) for j in self.List[i]])))