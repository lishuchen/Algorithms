#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# using siftdown
class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range(len(A) / 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, i):
        len_A = len(A)
        while 2 * i + 1 < len_A:
            child = 2 * i + 1
            child_right = child + 1
            if child_right < len_A and A[child_right] < A[child]:
                child = child_right

            if A[child] > A[i]:
                break

            A[child], A[i] = A[i], A[child]
            i = child

# using liftup
class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range(1, len(A)):
            self.siftup(A, i)

    def siftup(self, A, i):
        while i:
            father = (i - 1) / 2
            if A[father] < A[i]:
                break

            A[father], A[i] = A[i], A[father]
            i = father