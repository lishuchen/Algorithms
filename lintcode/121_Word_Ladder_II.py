#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # Write your code here
        dict.add(start)
        dict.add(end)

        pres = {word: [] for word in dict}

        cur = set([start])
        alphas = [chr(ord('a') + i) for i in range(26)]
        while cur and end not in cur:
            dict -= cur
            next = set()
            for word in cur:
                for i in range(len(word)):
                    for c in alphas:
                        new_w = word[:i] + c + word[i + 1:]
                        if new_w in dict and new_w not in cur:
                            pres[new_w].append(word)
                            next.add(new_w)
            cur = next

        rsl = []
        self.buildPath([], end, pres, rsl)
        return rsl

    def buildPath(self, cur, word, pres, rsl):
        if len(pres[word]) == 0:
            rsl.append([word] + cur)
            return
        for pr in pres[word]:
            self.buildPath([word] + cur, pr, pres, rsl)
