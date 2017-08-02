#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Greedy: O(n)
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return False

        farest = 0
        for i, num in enumerate(A):
            if i <= farest:
                farest = max(farest, i + num)
            else:
                return False

        return True


# DP: O(n ^ 2)
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return False

        ans = [False] * len(A)
        ans[0] = True
        for i in range(1, len(A)):
            for j in range(0, i):
                if ans[j] and A[j] + j >= i:
                    ans[i] = True
                    break

        return ans[-1]
