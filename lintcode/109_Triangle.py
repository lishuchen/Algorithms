#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Top - bottom
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """

    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0

        pre = triangle[0]
        for row in triangle[1:]:
            cur = list()
            for j in range(len(row)):
                if j == 0:
                    cur.append(row[0] + pre[0])
                elif j == len(row) - 1:
                    cur.append(row[-1] + pre[-1])
                else:
                    cur.append(min(pre[j - 1], pre[j]) + row[j])

            pre = cur

        return min(pre)


# bottom - top
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """

    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0

        pre = triangle[-1]
        for row in triangle[-2::-1]:
            cur = list()
            for j in range(len(row)):
                cur.append(min(pre[j], pre[j + 1]) + row[j])

            pre = cur

        return pre[0]
