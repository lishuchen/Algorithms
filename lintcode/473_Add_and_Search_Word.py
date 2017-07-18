#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.dct = dict()


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        if not word:
            return None

        node = self.root
        for ch in word:
            node = node.dct.setdefault(ch, TrieNode())

        node.is_end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        if not word:
            return False

        return self.search_word(self.root, word, 0)

    def search_word(self, node, word, i):
        if i == len(word):
            return node.is_end

        ch = word[i]
        if ch == '.':
            for c, next_node in node.dct.items():
                if self.search_word(next_node, word, i + 1):
                    return True
        else:
            if ch in node.dct:
                return self.search_word(node.dct[ch], word, i + 1)

        return False


        # Your WordDictionary object will be instantiated and called as such:
        # wordDictionary = WordDictionary()
        # wordDictionary.addWord("word")
        # wordDictionary.search("pattern")
