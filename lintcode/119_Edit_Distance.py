#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        if word1 is None and word2 is None:
            return None

        if len(word1) == 0:
            return len(word2)

        if len(word2) == 0:
            return len(word1)

        len_one = len(word1)
        len_two = len(word2)

        dis = [[0] * (len_two + 1) for _ in range(len_one + 1)]
        for i in range(len_one + 1):
            dis[i][0] = i
        for j in range(len_two + 1):
            dis[0][j] = j

        for i in range(1, len_one + 1):
            for j in range(1, len_two + 1):
                if word1[i - 1] == word2[j - 1]:
                    dis[i][j] = dis[i - 1][j - 1]
                else:
                    dis[i][j] = 1 + min(dis[i][j - 1], dis[i - 1][j], dis[i - 1][j - 1])

        return dis[len_one][len_two]
