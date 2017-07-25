#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None

        hp = []
        for lst in lists:
            if lst:
                heapq.heappush(hp, (lst.val, lst))

        cur = dummy_head = ListNode(-1)
        while hp:
            val, node = heapq.heappop(hp)
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heapq.heappush(hp, (node.val, node))

        return dummy_head.next
