#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.dct = dict()


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return

        node = self.root
        for ch in word:
            node = node.dct.setdefault(ch, TrieNode())

        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return None

        node = self.root
        for ch in word:
            if ch not in node.dct:
                return False
            node = node.dct[ch]

        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return None

        node = self.root
        for ch in prefix:
            if ch not in node.dct:
                return False
            node = node.dct[ch]

        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
