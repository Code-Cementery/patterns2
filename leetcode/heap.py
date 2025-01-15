import math
from heapq import nlargest
from statistics import mean
from typing import Literal


class MyHeap:
    def __init__(self, elements, which: Literal["min", "max"]):
        self.elements: list[float | int | None] = [None] + list(elements)
        self.heap_size = len(self.elements)
        self.construct = self.construct_max if which == "max" else self.construct_min

        # leave_indices = math.floor(self.heap_size/2 + 1), self.heap_size

        for i in range(self.parent(self.heap_size), 0, -1):
            self.construct(i)

    @classmethod
    def left(self, i):
        return 2*i

    @classmethod
    def right(self, i):
        return 2*i + 1

    @classmethod
    def parent(self, i):
        return i//2

    def construct_min(self, i=1):
        ileft = self.left(i)
        iright = self.right(i)
        iroot = i

        if ileft < self.heap_size and self.elements[ileft] < self.elements[iroot]:
            iroot = ileft
        if iright < self.heap_size and self.elements[iright] < self.elements[iroot]:
            iroot = iright

        if iroot != i:
            self.elements[i], self.elements[iroot] = self.elements[iroot], self.elements[i]

            self.construct_min(iroot)

    def construct_max(self, i=1):
        ileft = self.left(i)
        iright = self.right(i)
        iroot = i

        if ileft < self.heap_size and self.elements[ileft] > self.elements[iroot]:
            iroot = ileft
        if iright < self.heap_size and self.elements[iright] > self.elements[iroot]:
            iroot = iright

        if iroot != i:
            self.elements[i], self.elements[iroot] = self.elements[iroot], self.elements[i]

            self.construct_max(iroot)

    def sort(self, reversed=False):
        heap2 = MyHeap(self.elements[1:], "min" if reversed else "max")

        for i in range(heap2.heap_size-1, 1, -1):
            heap2.elements[i], heap2.elements[1] = heap2.elements[1], heap2.elements[i]
            heap2.heap_size = i

            heap2.construct()

        return heap2.elements[1:]
