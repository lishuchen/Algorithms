#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            dummy_head = cur = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next

                if root.right:
                    cur.next = root.right
                    cur = cur.next

                root = root.next

            root = dummy_head.next

        return None
