#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # find the middle of list
        end = mid = head
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        head2 = mid.next
        mid.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)

        return self.merge(l1, l2)

    def merge(self, l1, l2):
        head = ListNode(0)
        cur = head

        while l1 and l2:
            if l1.val < l2.val:
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

        return head.next
