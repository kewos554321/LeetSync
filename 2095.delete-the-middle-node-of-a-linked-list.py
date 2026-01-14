#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0, head)
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        if head == slow:
            head = slow.next
        return head

# @lc code=end

