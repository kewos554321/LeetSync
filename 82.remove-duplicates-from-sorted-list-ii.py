#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        prev.val = None
        prev.next = head
        
        head = prev
        curr = head.next
        dupl = False
        while curr:
            print('val=',curr.val)
            print(f'curr={curr}')
            if curr.next and curr.val == curr.next.val:
                dupl = True
            else:
                if dupl:
                    prev.next = curr.next
                    prev = curr.next
                    dupl = False
                else:
                    prev.next = curr
            curr = curr.next
 
        
        return head.next

# @lc code=end

