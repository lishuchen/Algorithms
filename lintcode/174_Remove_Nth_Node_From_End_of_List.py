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
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        p = q = dummy = ListNode(0)
        dummy.next = head

        for _ in range(n):
            q = q.next

        while q.next:
            q = q.next
            p = p.next

        p.next = p.next.next

        return dummy.next
