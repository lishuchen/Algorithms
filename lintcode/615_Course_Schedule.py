#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Topological sort
class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        if numCourses < 0:
            return False

        # indegree
        indegrees = [0] * numCourses

        # key: course val: a set of pres
        courses = dict()
        for relation in prerequisites:
            crs, pre = relation
            courses.setdefault(pre, []).append(crs)
            indegrees[crs] += 1

        zero_indgs = collections.deque()
        for num, v in enumerate(indegrees):
            if v == 0:
                zero_indgs.append(num)

        while zero_indgs:
            node = zero_indgs.popleft()
            if node in courses:
                for num in courses[node]:
                    indegrees[num] -= 1
                    if indegrees[num] == 0:
                        zero_indgs.append(num)

        for v in indegrees:
            if v != 0:
                return False

        return True
