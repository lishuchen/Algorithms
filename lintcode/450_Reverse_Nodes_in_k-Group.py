#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if not head:
            return None

        if k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        while start:
            end = start
            count = 0
            for _ in range(k):
                if end.next:
                    count += 1
                    end = end.next
                else:
                    break

            # not enough
            if count != k:
                break

            next_start = start.next

            for _ in range(k - 1):
                cur = start.next
                start.next = cur.next
                cur.next = end.next
                end.next = cur

            start = next_start

        return dummy.next
