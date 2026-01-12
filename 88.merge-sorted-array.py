#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0    
        j = 0
        
        while j < len(nums2 or i < len(nums1)):
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            else:
                i += 1
        while j < len(nums2):
            nums1[i].append(nums2[j])
            j += 1
        print(nums1)
        
# @lc code=end

