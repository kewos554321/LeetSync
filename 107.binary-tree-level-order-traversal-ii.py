#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        s = [[root]]
        res = []
        while s:
            l = s.pop(0)
            temp_s = []
            temp_res = []
            for n in l:
                temp_res.append(n.val)
                if n.left:
                    temp_s.append(n.left)
                if n.right:
                    temp_s.append(n.right)
            if temp_s:
                s.append(temp_s)
            if temp_res:
                res.append(temp_res)
        return res[::-1]
        
# @lc code=end

