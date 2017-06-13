#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Solution 1:
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0

        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    count += 1
                    self.mask(board, i, j)

        return count

    def search(self, board, i, j):
        board[i][j] = '.'
        k = j + 1
        while k < len(board[i]) and board[i][k] == 'X':
            board[i][k] = '.'
            k += 1

        i += 1
        while i < len(board) and board[i][j] == 'X':
            board[i][j] = '.'
            i += 1


# Solution 2:
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0

        count = 0
        offsets = [[-1, 0], [0, +1]]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    if (0 < i and board[i - 1][j] == 'X') or (0 < j and board[i][j - 1] == 'X'):
                        continue
                    count += 1

        return count
