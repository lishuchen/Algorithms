#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# greedy
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        if not courses:
            return None

        cours = sorted(courses, key=lambda x: x[1])
        start = 0
        max_hp = []
        for time, end in cours:
            start += time
            heapq.heappush(max_hp, -time)
            while start > end:
                start += heapq.heappop(max_hp)

        return len(max_hp)
