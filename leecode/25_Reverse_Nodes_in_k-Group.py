#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        new_hd = ListNode(0)
        new_hd.next = head
        start = end = new_hd

        while end.next:
            count = 0
            for _ in range(k):
                if end.next:
                    end = end.next
                    count += 1
                else:
                    break

            if count == k:
                tmp = None
                for i in range(k - 1):
                    cur = start.next
                    start.next = cur.next
                    cur.next = end.next
                    end.next = cur
                    if i == 0:
                        tmp = cur

                if tmp:
                    start = end = tmp

        return new_hd.next
