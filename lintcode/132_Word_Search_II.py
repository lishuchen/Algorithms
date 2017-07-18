#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TrieNode:
    def __init__(self):
        self.dct = dict()
        self.is_end = False


class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []

        # build trie
        self.root = TrieNode()
        for word in words:
            self.build_trie(word)

        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.visit = [[False] * self.cols for _ in range(self.rows)]
        self.rsl = set()
        for i in range(self.rows):
            for j in range(self.cols):
                self.search(i, j, self.root, "")

        return list(self.rsl)

    def search(self, i, j, node, word):
        if node.is_end:
            self.rsl.add(word)

        if -1 < i < self.rows and -1 < j < self.cols and self.visit[i][j] == False:
            self.visit[i][j] = True
            ch = self.board[i][j]
            if ch in node.dct:
                offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for x, y in offsets:
                    self.search(i + x, j + y, node.dct[ch], word + ch)
            self.visit[i][j] = False

    def build_trie(self, word):
        node = self.root
        for ch in word:
            node = node.dct.setdefault(ch, TrieNode())

        node.is_end = True
