#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        new_head = ListNode(0)
        new_head.next = head
        fst = snd = new_head
        while fst.next and fst.next.next:
            fst = fst.next.next
            snd.next.next = fst.next
            fst.next = snd.next
            snd.next = fst
            snd = fst = fst.next

        return new_head.next
