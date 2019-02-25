from __future__ import print_function
import math

class SegmentTree:
    
    def __init__(self, A):
        self.A = A
        self.N = len(A)
        self.st = [0] * (4 * self.N) # approximate the overall size of segment tree with array N
        self.build(1, 0, self.N - 1)
        
    def left(self, idx):
        return idx * 2

    def right(self, idx):
        return idx * 2 + 1

    def build(self, idx, l, r):
        if l == r:
            self.st[idx] = self.A[l]
        else:
            mid = (l + r) // 2
            self.build(self.left(idx), l, mid)
            self.build(self.right(idx), mid + 1, r)
            self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
    
    def update(self, a, b, val):
        return self.update_recursive(1, 0, self.N - 1, a - 1, b - 1, val)
    
    def update_recursive(self, idx, l, r, a, b, val): # update(1, 1, N, a, b, v) for update val v to [a,b]
        if r < a or l > b:
            return True
        if l == r :
            self.st[idx] = val
            return True
        mid = (l+r)//2
        self.update_recursive(self.left(idx), l, mid, a, b, val)
        self.update_recursive(self.right(idx), mid+1, r, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
        return True

    def query(self, a, b):
        return self.query_recursive(1, 0, self.N - 1, a - 1, b - 1)

    def query_recursive(self, idx, l, r, a, b): #query(1, 1, N, a, b) for query max of [a,b]
        if r < a or l > b:
            return float('-inf')
        if l >= a and r <= b:
            return self.st[idx]
        mid = (l+r)//2
        q1 = self.query_recursive(self.left(idx), l, mid, a, b)
        q2 = self.query_recursive(self.right(idx), mid + 1, r, a, b)
        return max(q1, q2)

    def showData(self):
        showList = []
        for i in range(1,N+1):
            showList += [self.query(i, i)]
        print (showList)
            
