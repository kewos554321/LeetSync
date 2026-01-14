#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head
        if c.next:
            n = c.next
        else:
            return head

        head = n

        while c and n:
            print(c.val, n.val)
            nn = n.next
            c.next = nn
            n.next = c

            if not nn.next:
                return

            c = nn
            n = nn.next

        return head

# @lc code=end

