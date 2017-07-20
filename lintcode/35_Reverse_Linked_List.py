#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# one
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """

    def reverse(self, head):
        # write your code here
        l = dummy_head = ListNode(0)
        dummy_head.next = head

        count = 0
        while l.next:
            count += 1
            l = l.next

        for _ in range(count - 1):
            tmp = dummy_head.next.next
            dummy_head.next.next = l.next
            l.next = dummy_head.next
            dummy_head.next = tmp

        return dummy_head.next


# two
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """

    def reverse(self, head):
        # write your code here
        cur = None
        while head:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp

        return cur
