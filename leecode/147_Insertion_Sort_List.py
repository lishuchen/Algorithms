#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        new_head = ListNode(0)

        while head:
            ptr = new_head
            while ptr.next and ptr.next.val < head.val:
                ptr = ptr.next
            tmp = ptr.next
            ptr.next = head
            head = head.next
            ptr.next.next = tmp

        return new_head.next
