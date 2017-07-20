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
    @param head: A ListNode
    @return: A ListNode
    """

    def deleteDuplicates(self, head):
        # write your code here

        start = end = head

        while end:
            if end.val == start.val:
                end = end.next
            else:
                start.next = end
                start = end

        if start:
            start.next = None

        return head
