#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None

        cur = head
        dct = dict()
        while cur:
            dct[cur] = RandomListNode(cur.label)
            cur = cur.next

        new_cur = new_hd = RandomListNode(-1)
        cur = head
        while cur:
            new_cur.next = dct[cur]
            new_cur = new_cur.next
            if cur.random:
                new_cur.random = dct[cur.random]
            cur = cur.next

        return new_hd.next
