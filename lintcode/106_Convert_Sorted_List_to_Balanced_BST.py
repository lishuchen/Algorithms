#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        # write your code here
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        mid_pre = None
        fast = mid = head
        while fast and fast.next:
            mid_pre = mid
            fast = fast.next.next
            mid = mid.next

        if mid_pre:
            mid_pre.next = None

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
