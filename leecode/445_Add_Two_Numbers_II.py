#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy_head = ListNode(0)
        flag = 0
        while l1 or l2 or flag:
            val = flag
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            flag, val = divmod(val, 10)
            node = ListNode(val)
            node.next = dummy_head.next
            dummy_head.next = node

        return dummy_head.next

    def reverse(self, head):
        dummy_hd = ListNode(0)
        while head:
            next_node = head.next
            head.next = dummy_hd.next
            dummy_hd.next = head
            head = next_node

        return dummy_hd.next
