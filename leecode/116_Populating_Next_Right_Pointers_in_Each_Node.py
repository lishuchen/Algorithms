#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# Solution 1： level-order
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None

        while root.left:
            node = root
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            root = root.left


# Solution 2
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None

        dq = collections.deque()
        dq.append(root)
        while dq:
            size = len(dq)
            next_one = None
            for _ in range(size):
                node = dq.popleft()
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
                node.next = next_one
                next_one = node
