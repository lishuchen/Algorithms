#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: iteration
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        dq = collections.deque()
        dq.append(root)
        count = 1
        while dq:
            size = len(dq)
            while size:
                node = dq.popleft()
                if not node.left and not node.right:
                    return count
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                size -= 1
            count += 1

        return count


# Solution 2: recursion
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
