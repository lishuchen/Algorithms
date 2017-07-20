#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        dummy_head = ListNode(0)
        l = dummy_head

        flag = 0
        while l1 or l2 or flag:
            val = flag
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            flag, v = divmod(val, 10)
            node = ListNode(v)
            l.next = node
            l = l.next

        return dummy_head.next
