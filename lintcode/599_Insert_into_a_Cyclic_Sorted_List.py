#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node
    def insert(self, node, x):
        # Write your code here
        # Write your code here
        if node is None:
            node = ListNode(x)
            node.next = node
            return node

        cur = node
        while True:
            if x <= cur.next.val and x >= cur.val:
                break
            if (cur.val > cur.next.val) and (x < cur.next.val or x > cur.val):
                break
            if cur.next is node:
                break

            cur = cur.next

        newNode = ListNode(x)
        newNode.next = cur.next
        cur.next = newNode

        return newNode
