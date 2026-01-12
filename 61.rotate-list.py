#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None: return head
        if head.next is None: return head


        curr = head

        length = 0

        while True:
            length += 1
            if curr.next is None:
                curr.next = head
                break
            curr = curr.next

        targetIndex = length - (k % length) - 1

        while True:
            targetIndex -= 1
            if targetIndex >= 0:
                head = head.next
            else:
                newHead = head.next
                head.next = None
                return newHead


        
# @lc code=end

