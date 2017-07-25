#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        if n <= 0:
            return -1

        primes = [2, 3, 5]
        hp = [1]
        pre = num = None
        while n:
            num = heapq.heappop(hp)

            if num == pre:
                continue

            n -= 1
            pre = num
            for prime in primes:
                heapq.heappush(hp, num * prime)

        return num
