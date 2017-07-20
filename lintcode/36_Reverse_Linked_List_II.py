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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        if not head:
            return None

        p = q = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next

        for _ in range(n):
            q = q.next

        for _ in range(n - m):
            tmp = p.next.next
            p.next.next = q.next
            q.next = p.next
            p.next = tmp

        return dummy.next
