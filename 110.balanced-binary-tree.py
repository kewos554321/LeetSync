#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        if abs(self.calcHeight(root.left) - self.calcHeight(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def calcHeight(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        return 1 + max(self.calcHeight(node.left), self.calcHeight(node.right))
# @lc code=end

