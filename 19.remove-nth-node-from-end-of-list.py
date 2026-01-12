#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = {}
        temp = head
        i = 0
        while temp:
            i+=1
            m[i] = temp
            temp = temp.next

        if i - n == 0:
            return head.next
        
        if n == 1:
            if i == 1:
                return []
            else:
                m[i-n].next = None
        
        else:
            m[i-n].next = m[i-n+2]

        return head

        
# @lc code=end

