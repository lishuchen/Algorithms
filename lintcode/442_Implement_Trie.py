#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""


class TrieNode:
    def __init__(self):
        # Initialize your data structure here.
        self.is_word = False
        self.dct = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.dct.setdefault(ch, TrieNode())
        node.is_word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.dct:
                return False
            node = node.dct[ch]
        return node.is_word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.dct:
                return False
            node = node.dct[ch]
        return True
