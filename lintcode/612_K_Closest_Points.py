#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import heapq


class Node:
    def __init__(self, dis, pt):
        self.dis = dis
        self.point = pt

    def __lt__(self, other):
        if other.dis != self.dis:
            return self.dis < other.dis
        if other.point.x != self.point.x:
            return self.point.x < other.point.x

        return self.point.y < other.point.y


class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        hp = []

        for pt in points:
            dis = (pt.x - origin.x) ** 2 + (pt.y - origin.y) ** 2
            heapq.heappush(hp, Node(dis, pt))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(hp).point)

        return topk
