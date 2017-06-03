#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        positions = sorted({t for bld in buildings for t in (bld[0], bld[1])})
        hp = []
        rsl = [[-1, -1]]
        i = 0
        for pos in positions:
            while i < len(buildings) and buildings[i][0] == pos:
                heapq.heappush(hp, [-buildings[i][2], buildings[i][1]])
                i += 1
            while hp and hp[0][1] <= pos:
                heapq.heappop(hp)
            if hp and -hp[0][0] != rsl[-1][1]:
                rsl.append([pos, -hp[0][0]])
            if not hp:
                rsl.append([pos, 0])

        return rsl[1:]

if __name__ == "__main__":
    s = Solution()
    print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))