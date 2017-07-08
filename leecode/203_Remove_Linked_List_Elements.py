#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = new_head = ListNode(0)
        while head:
            if head.val != val:
                ptr.next = head
                ptr = ptr.next
            head = head.next
        ptr.next = None

        return new_head.next
