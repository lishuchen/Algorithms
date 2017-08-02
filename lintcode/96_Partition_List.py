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
    @param x: an integer
    @return: a ListNode
    """

    def partition(self, head, x):
        # write your code here
        if not head:
            return None

        small_head = small = ListNode(-1)
        large_head = large = ListNode(-1)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next

            head = head.next

        large.next = None
        small.next = large_head.next

        return small_head.next
