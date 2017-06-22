#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        frst_ptr = scnd_ptr = head
        for _ in range(n):
            frst_ptr = frst_ptr.next

        # delete head:
        if frst_ptr == None:
            if head.next == None:
                return []
            else:
                return head.next

        while frst_ptr and frst_ptr.next:
            frst_ptr = frst_ptr.next
            scnd_ptr = scnd_ptr.next

        scnd_ptr.next = scnd_ptr.next.next

        return head
