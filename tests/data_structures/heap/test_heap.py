from data_structures.heap.heap import Heap

class TestHeap:
    
    def test_heap_1(self):
        l = [4,5,3,6,2,7,1]
        h = Heap()
        h.buildHeap(l)
        h.heapSort()
        assert h.h == [1,2,3,4,5,6,7]