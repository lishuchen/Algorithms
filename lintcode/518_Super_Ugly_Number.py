#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        if n <= 1:
            return n

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
