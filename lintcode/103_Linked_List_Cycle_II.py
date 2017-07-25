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
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here
        if not head:
            return None

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                ant = head
                while ant != slow:
                    ant = ant.next
                    slow = slow.next
                return ant

        return None
