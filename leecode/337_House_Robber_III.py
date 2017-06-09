# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.robber(root)[1]

    def robber(self, root):
        if not root:
            # [not robbed, robbed]
            return [0, 0]
        lf = self.robber(root.left)
        rg = self.robber(root.right)

        # need to compare these two, even root is robbed
        return [lf[1] + rg[1], max(lf[1] + rg[1], root.val + lf[0] + rg[0])]