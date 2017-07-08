#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        make = lambda x: [x.val, x]
        ptr = head = ListNode(0)
        hp = []
        for node in lists:
            if node:
                heapq.heappush(hp, make(node))

        while hp:
            _, node = heapq.heappop(hp)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                heapq.heappush(hp, make(node.next))

        return head.next
