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
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None and l2 is None:
            return None

        dummy_head = ListNode(-1)
        cur = dummy_head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy_head.next
