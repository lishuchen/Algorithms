#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class DLinkNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.map = dict()
        self.head = DLinkNode(-1, -1)
        self.end = DLinkNode(-1, -1)

        self.head.next = self.end
        self.end.pre = self.head

    def _update(self, node):
        if node.next == self.end:
            return

        node.pre.next = node.next
        node.next.pre = node.pre

        node.next = self.end
        node.pre = self.end.pre
        node.pre.next = node
        self.end.pre = node

    def _remove(self):
        node = self.head.next
        self.head.next = node.next
        node.next.pre = self.head

        key = node.key
        del node
        return key

    def _insert(self, node):
        node.next = self.end
        node.pre = self.end.pre
        self.end.pre.next = node
        self.end.pre = node

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.map:
            return -1

        node = self.map[key]
        self._update(node)
        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._update(node)
        else:
            if len(self.map) >= self.capacity:
                rm_key = self._remove()
                del self.map[rm_key]

            node = DLinkNode(key, value)
            self.map[key] = node
            self._insert(node)
