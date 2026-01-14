#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oh = ListNode(0, None)
        odd = oh
        eh = ListNode(0, None)
        even = eh
        curr = head
        switch = True
        while curr:
            if switch:
                odd.next = curr
                odd = odd.next
                curr = curr.next
                switch = False
            else:
                even.next = curr
                even = even.next
                curr = curr.next
                switch = True
        even.next = None
        odd.next = eh.next
        return oh.next

            
# @lc code=end

