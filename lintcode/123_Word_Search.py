#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if not board and not word:
            return False

        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.search(board, word, visited, i, j, 0):
                    return True

        return False

    def search(self, board, word, visited, i, j, index):
        if index == len(word):
            return True

        if -1 < i < len(board) and -1 < j < len(board[0]) and visited[i][j] == False:
            if board[i][j] == word[index]:
                visited[i][j] = True
                offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for x, y in offsets:
                    if self.search(board, word, visited, i + x, j + y, index + 1):
                        return True
                visited[i][j] = False

        return False
