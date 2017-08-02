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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """

    def sortList(self, head):
        # write your code here
        if not head:
            return None

        if not head.next:
            return head

        mid_pre = None
        mid = end = head
        while end and end.next:
            end = end.next.next
            mid_pre = mid
            mid = mid.next

        if mid:
            mid_pre.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        cur = dummy = ListNode(-1)
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next
