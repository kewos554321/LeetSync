# LeetCode Practice Plan

## Progress Overview

**已完成:** 24 題
**待完成:** 18 題

---

## Completed Problems (已完成)

| # | Problem | Category | Technique |
|---|---------|----------|-----------|
| 1 | Two Sum | Array/Hash | Hash Map |
| 2 | Add Two Numbers | Linked List | Iteration |
| 7 | Reverse Integer | Math | Digit Manipulation |
| 9 | Palindrome Number | Math | Two Pointers |
| 15 | 3Sum | Array | Two Pointers + Sort |
| 19 | Remove Nth Node From End | Linked List | Two Pointers |
| 56 | Merge Intervals | Array | Sorting + Merge |
| 58 | Length of Last Word | String | Split |
| 75 | Sort Colors | Array | Dutch National Flag |
| 78 | Subsets | Backtracking | Recursion |
| 82 | Remove Duplicates II | Linked List | Two Pointers |
| 88 | Merge Sorted Array | Array | Two Pointers |
| 94 | Binary Tree Inorder | Tree | DFS Recursion |
| 102 | Level Order Traversal | Tree | BFS Queue |
| 107 | Level Order II | Tree | BFS Queue |
| 110 | Balanced Binary Tree | Tree | DFS Height |
| 125 | Valid Palindrome | String | Two Pointers |
| 136 | Single Number | Bit | XOR |
| 144 | Binary Tree Preorder | Tree | DFS Recursion |
| 145 | Binary Tree Postorder | Tree | DFS Recursion |
| 198 | House Robber | DP | Space Optimized DP |
| 206 | Reverse Linked List | Linked List | Iteration |
| 226 | Invert Binary Tree | Tree | Recursion |
| 283 | Move Zeroes | Array | Two Pointers |

---

## Incomplete Problems (待完成)

### Priority 1: Core Algorithms (核心演算法)

| # | Problem | Category | Key Concept |
|---|---------|----------|-------------|
| 53 | Maximum Subarray | DP/Array | **Kadane's Algorithm** |
| 5 | Longest Palindromic Substring | DP/String | Expand Around Center / DP |
| 39 | Combination Sum | Backtracking | DFS with Pruning |
| 131 | Palindrome Partitioning | Backtracking | DFS + Palindrome Check |
| 105 | Construct Binary Tree | Tree | Preorder/Inorder Property |

### Priority 2: Classic Problems (經典題目)

| # | Problem | Category | Key Concept |
|---|---------|----------|-------------|
| 35 | Search Insert Position | Binary Search | Lower Bound |
| 50 | Pow(x, n) | Math | Fast Power (Binary Exponentiation) |
| 48 | Rotate Image | Matrix | Layer by Layer / Transpose+Reverse |
| 54 | Spiral Matrix | Matrix | Direction Simulation |
| 57 | Insert Interval | Interval | Merge Logic |
| 63 | Unique Paths II | DP | 2D Grid DP |

### Priority 3: Linked List (鏈結串列)

| # | Problem | Category | Key Concept |
|---|---------|----------|-------------|
| 61 | Rotate List | Linked List | Cycle + Split |
| 83 | Remove Duplicates | Linked List | Single Pointer |
| 92 | Reverse Linked List II | Linked List | Partial Reverse |

### Priority 4: Others (其他)

| # | Problem | Category | Key Concept |
|---|---------|----------|-------------|
| 14 | Longest Common Prefix | String | Vertical/Horizontal Scan |
| 29 | Divide Two Integers | Math | Bit Manipulation |
| 45 | Jump Game II | Greedy | BFS / Greedy Jump |
| 67 | Add Binary | String | Carry Addition |

---

## Review Plan (複習計劃)

### Week 1: Dynamic Programming & Greedy

- [ ] **Day 1-2:** 53. Maximum Subarray (Kadane's Algorithm)
  - 複習概念: 局部最優 → 全局最優
  - 延伸: 變體 - 返回子陣列本身

- [ ] **Day 3-4:** 5. Longest Palindromic Substring
  - 複習概念: 中心擴展法 / DP 二維表
  - 延伸: Manacher's Algorithm (進階)

- [ ] **Day 5:** 63. Unique Paths II
  - 複習概念: 2D DP with obstacles

- [ ] **Day 6-7:** 45. Jump Game II
  - 複習概念: Greedy / BFS 思維

### Week 2: Backtracking

- [ ] **Day 1-2:** 39. Combination Sum
  - 複習概念: 回溯模板、剪枝

- [ ] **Day 3-4:** 131. Palindrome Partitioning
  - 複習概念: 回溯 + 回文判斷

- [ ] **Day 5-7:** 複習 78. Subsets (已完成)
  - 對比不同回溯題型

### Week 3: Tree & Binary Search

- [ ] **Day 1-2:** 105. Construct Binary Tree
  - 複習概念: Preorder 第一個是 root, Inorder 分割左右

- [ ] **Day 3-4:** 35. Search Insert Position
  - 複習概念: 二分查找邊界條件

- [ ] **Day 5-7:** 複習已完成的 Tree 題 (94, 102, 144, 145)

### Week 4: Linked List & Matrix

- [ ] **Day 1-2:** 92. Reverse Linked List II
  - 複習概念: 部分反轉技巧

- [ ] **Day 3:** 83. Remove Duplicates
- [ ] **Day 4:** 61. Rotate List

- [ ] **Day 5-6:** 48. Rotate Image + 54. Spiral Matrix
  - 複習概念: 矩陣操作技巧

- [ ] **Day 7:** 57. Insert Interval

---

## Quick Reference: Algorithm Templates

### Kadane's Algorithm (53)
```python
def maxSubArray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

### Backtracking Template (39, 131)
```python
def backtrack(start, path, target):
    if condition:
        result.append(path[:])
        return
    for i in range(start, len(candidates)):
        path.append(candidates[i])
        backtrack(i, path, target - candidates[i])  # 可重複
        # backtrack(i+1, path, ...)  # 不可重複
        path.pop()
```

### Binary Search Template (35)
```python
def searchInsert(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l
```

---

---

## LeetCode Must-Do List (經典必刷題)

### Array & Hash Table

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 1 | Two Sum | Easy | Done |
| 26 | Remove Duplicates from Sorted Array | Easy | TODO |
| 27 | Remove Element | Easy | TODO |
| 49 | Group Anagrams | Medium | TODO |
| 128 | Longest Consecutive Sequence | Medium | TODO |
| 238 | Product of Array Except Self | Medium | TODO |
| 347 | Top K Frequent Elements | Medium | TODO |

### Two Pointers

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 11 | Container With Most Water | Medium | TODO |
| 42 | Trapping Rain Water | Hard | TODO |
| 167 | Two Sum II | Medium | TODO |
| 344 | Reverse String | Easy | TODO |

### Sliding Window

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 3 | Longest Substring Without Repeating | Medium | TODO |
| 76 | Minimum Window Substring | Hard | TODO |
| 239 | Sliding Window Maximum | Hard | TODO |
| 424 | Longest Repeating Character Replacement | Medium | TODO |

### Binary Search

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 33 | Search in Rotated Sorted Array | Medium | TODO |
| 34 | Find First and Last Position | Medium | TODO |
| 74 | Search a 2D Matrix | Medium | TODO |
| 153 | Find Minimum in Rotated Sorted Array | Medium | TODO |
| 704 | Binary Search | Easy | TODO |

### Linked List

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 21 | Merge Two Sorted Lists | Easy | TODO |
| 23 | Merge k Sorted Lists | Hard | TODO |
| 141 | Linked List Cycle | Easy | TODO |
| 142 | Linked List Cycle II | Medium | TODO |
| 143 | Reorder List | Medium | TODO |
| 146 | LRU Cache | Medium | TODO |
| 287 | Find the Duplicate Number | Medium | TODO |

### Stack

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 20 | Valid Parentheses | Easy | TODO |
| 84 | Largest Rectangle in Histogram | Hard | TODO |
| 155 | Min Stack | Medium | TODO |
| 739 | Daily Temperatures | Medium | TODO |

### Tree

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 98 | Validate Binary Search Tree | Medium | TODO |
| 100 | Same Tree | Easy | TODO |
| 104 | Maximum Depth of Binary Tree | Easy | TODO |
| 124 | Binary Tree Maximum Path Sum | Hard | TODO |
| 199 | Binary Tree Right Side View | Medium | TODO |
| 230 | Kth Smallest Element in BST | Medium | TODO |
| 235 | LCA of BST | Medium | TODO |
| 236 | LCA of Binary Tree | Medium | TODO |
| 543 | Diameter of Binary Tree | Easy | TODO |
| 572 | Subtree of Another Tree | Easy | TODO |

### Heap / Priority Queue

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 215 | Kth Largest Element | Medium | TODO |
| 295 | Find Median from Data Stream | Hard | TODO |
| 355 | Design Twitter | Medium | TODO |

### Graph

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 133 | Clone Graph | Medium | TODO |
| 200 | Number of Islands | Medium | TODO |
| 207 | Course Schedule | Medium | TODO |
| 210 | Course Schedule II | Medium | TODO |
| 417 | Pacific Atlantic Water Flow | Medium | TODO |
| 684 | Redundant Connection | Medium | TODO |
| 743 | Network Delay Time | Medium | TODO |

### Dynamic Programming

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 62 | Unique Paths | Medium | TODO |
| 70 | Climbing Stairs | Easy | TODO |
| 91 | Decode Ways | Medium | TODO |
| 139 | Word Break | Medium | TODO |
| 152 | Maximum Product Subarray | Medium | TODO |
| 213 | House Robber II | Medium | TODO |
| 300 | Longest Increasing Subsequence | Medium | TODO |
| 322 | Coin Change | Medium | TODO |
| 416 | Partition Equal Subset Sum | Medium | TODO |
| 494 | Target Sum | Medium | TODO |
| 1143 | Longest Common Subsequence | Medium | TODO |

### Greedy

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 55 | Jump Game | Medium | TODO |
| 134 | Gas Station | Medium | TODO |
| 763 | Partition Labels | Medium | TODO |

### Intervals

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 252 | Meeting Rooms | Easy | TODO |
| 253 | Meeting Rooms II | Medium | TODO |
| 435 | Non-overlapping Intervals | Medium | TODO |

### Bit Manipulation

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 190 | Reverse Bits | Easy | TODO |
| 191 | Number of 1 Bits | Easy | TODO |
| 268 | Missing Number | Easy | TODO |
| 338 | Counting Bits | Easy | TODO |
| 371 | Sum of Two Integers | Medium | TODO |

### Trie

| # | Problem | Difficulty | Status |
|---|---------|------------|--------|
| 208 | Implement Trie | Medium | TODO |
| 211 | Design Add and Search Words | Medium | TODO |
| 212 | Word Search II | Hard | TODO |

---

## Recommended Study Path

### Phase 1: Foundation (基礎鞏固) - 2 weeks
1. 完成目前檔案中的 **待完成題目**
2. 練習 Easy 題目打基礎
3. 重點: Array, Hash Table, Two Pointers

### Phase 2: Core Patterns (核心模式) - 4 weeks
1. **Week 1-2:** Binary Search + Sliding Window
2. **Week 3-4:** Tree DFS/BFS + Graph Basics

### Phase 3: Advanced (進階挑戰) - 4 weeks
1. **Week 1-2:** Dynamic Programming
2. **Week 3-4:** Stack (Monotonic), Heap, Trie

### Phase 4: Mock Interview (模擬面試)
1. 計時練習 (45 min/題)
2. 混合類型題目
3. 口頭解釋思路

---

## Quick Start Checklist

### 今日任務
- [ ] 完成 53. Maximum Subarray (Kadane's Algorithm)

### 本週目標 (選 5 題)
- [ ] 53. Maximum Subarray
- [ ] 5. Longest Palindromic Substring
- [ ] 3. Longest Substring Without Repeating Characters
- [ ] 21. Merge Two Sorted Lists
- [ ] 20. Valid Parentheses

### 重要複習
- [ ] 回顧 198. House Robber 的 DP 思維
- [ ] 回顧 78. Subsets 的回溯模板
- [ ] 回顧 102. Level Order Traversal 的 BFS 模板
