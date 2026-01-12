# LeetCode 學習日誌

這是一個紀錄你解決 LeetCode 問題的日誌。每個問題都遵循一個固定的模板，幫助你深入理解問題、思考解法並記錄學習心得。

---

## 模板（請複製此模板來記錄每個新問題）

### [題號]. [題目名稱]

- **連結:** [貼上題目連結]
- **標籤:** `Array`, `Two Pointers`, `Sliding Window`
- **日期:** 2026-01-12

#### 1. 問題理解 (Problem Understanding)
> *用你自己的話簡述題目要求。*
> *限制條件 (Constraints) 有哪些？例如：陣列長度、數值範圍等。*
> *有哪些需要考慮的邊界情況 (Edge Cases)？例如：空陣列、單一元素、重複值等。*

#### 2. 初步想法 & 暴力解 (Initial Thoughts & Brute-Force)
> *你第一時間想到的解法是什麼？*
> *這個解法的時間複雜度和空間複雜度是多少？*
> *寫下或貼上你的暴力解程式碼（如果有的話）。*

```python
# (如果適用) 暴力解的程式碼
```

#### 3. 最優解 (Optimal Solution)
> *這個問題的核心觀念/模式是什麼？(例如：滑動窗口、雙指針、動態規劃、雜湊表查找)*
> *優化解法的思路是什麼？*
> *演算法的步驟是什麼？*
>
> 1.  步驟一
> 2.  步驟二
> 3.  ...

- **時間複雜度:** O(...)
- **空間複雜度:** O(...)

```python
# 最優解的程式碼
```

#### 4. 關鍵心得 & 延伸 (Key Takeaways & Connections)
> *從這個問題中學到了什麼關鍵技巧？*
> *這個核心觀念可以用在哪些其他類型的問題上？*
> *有沒有其他類似的題目可以一起練習？*

---

## 範例：1. Two Sum

### 1. Two Sum

- **連結:** https://leetcode.com/problems/two-sum/
- **標籤:** `Array`, `Hash Table`
- **日期:** 2026-01-12

#### 1. 問題理解 (Problem Understanding)
> 給定一個整數陣列 `nums` 和一個目標值 `target`，找出陣列中哪兩個數字的總和等於 `target`，並返回它們的索引。
> **Constraints:** 陣列長度 `2 <= nums.length <= 10^4`，數字範圍 `-10^9 <= nums[i] <= 10^9`，`target` 範圍也相同。保證只有一個唯一解。
> **Edge Cases:** 數字可能為負數。

#### 2. 初步想法 & 暴力解 (Initial Thoughts & Brute-Force)
> 最直觀的方法是使用兩層迴圈。外層迴圈遍歷每個元素 `nums[i]`，內層迴圈遍歷 `nums[j]` (其中 `j > i`)，檢查 `nums[i] + nums[j]` 是否等於 `target`。
> 時間複雜度是 O(n^2)，空間複雜度是 O(1)。

```python
def twoSum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

#### 3. 最優解 (Optimal Solution)
> 核心觀念是「用空間換取時間」。我們可以遍歷一次陣列，同時使用一個雜湊表 (Hash Map / Dictionary) 來儲存已經看過的數字及其索引。
>
> 演算法步驟：
> 1. 建立一個空的雜湊表 `seen`。
> 2. 遍歷陣列 `nums` 中的每個數字 `num` 及其索引 `i`。
> 3. 計算我們需要的「補充數」 `complement = target - num`。
> 4. 檢查 `complement` 是否已經存在於 `seen` 雜湊表中。
> 5. 如果存在，代表我們找到了配對，返回 `[seen[complement], i]`。
> 6. 如果不存在，將當前的 `num` 和其索引 `i` 存入 `seen` 雜湊表中，以便後續的數字查找。

- **時間複雜度:** O(n)，因為我們只需要遍歷陣列一次。雜湊表的查找和插入操作平均是 O(1)。
- **空間複雜度:** O(n)，在最壞的情況下，我們需要將所有數字都存入雜湊表。

```python
def twoSum_optimal(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

#### 4. 關鍵心得 & 延伸 (Key Takeaways & Connections)
> 當題目要求在一個集合中尋找兩個元素的關係時（例如和、差），雜湊表是一個非常強大的工具，可以將時間複雜度從 O(n^2) 降到 O(n)。
> 這種「查找補充數」的模式非常經典。
> **相關題目:** 15. 3Sum, 18. 4Sum 等問題都是這個概念的延伸。

---

## 20. Valid Parentheses

### 20. Valid Parentheses

- **連結:** https://leetcode.com/problems/valid-parentheses/
- **標籤:** `String`, `Stack`
- **日期:** 2026-01-12

#### 1. 問題理解 (Problem Understanding)
> 給定一個只包含 `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'` 的字串，判斷該字串是否有效。
> 有效的條件：
> 1. 左括號必須用相同類型的右括號閉合。
> 2. 左括號必須以正確的順序閉合。
> 3. 每個右括號都有一個對應的相同類型的左括號。
>
> **Constraints:** 字串長度 `1 <= s.length <= 10^4`，字串只包含括號字元。
> **Edge Cases:** 空字串（視為有效）、只有左括號、只有右括號、括號類型不匹配。

#### 2. 初步想法 & 暴力解 (Initial Thoughts & Brute-Force)
> 可以反覆掃描字串，每次找到一對相鄰的匹配括號就移除它，直到字串為空（有效）或無法再移除（無效）。
> 時間複雜度是 O(n^2)，空間複雜度是 O(n)。

#### 3. 最優解 (Optimal Solution)
> 核心觀念是使用**堆疊 (Stack)**。遇到左括號就入棧，遇到右括號就檢查棧頂是否為對應的左括號。
>
> 演算法步驟：
> 1. 建立一個空的堆疊 `stack`。
> 2. 遍歷字串中的每個字元 `char`。
> 3. 如果 `char` 是左括號 `(`, `[`, `{`，將其推入堆疊。
> 4. 如果 `char` 是右括號：
>    - 檢查堆疊是否為空，若為空則返回 `False`。
>    - 檢查堆疊頂端是否為對應的左括號，若不是則返回 `False`。
>    - 若匹配，則彈出堆疊頂端元素。
> 5. 遍歷結束後，檢查堆疊是否為空。若為空則有效，否則無效。

- **時間複雜度:** O(n)，只需遍歷字串一次。
- **空間複雜度:** O(n)，最壞情況下堆疊會存放所有左括號。

```python
def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in '{[(':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            if char == ')' and stack[-1] != '(':
                return False
            stack.pop()
    return not stack
```

#### 4. 關鍵心得 & 延伸 (Key Takeaways & Connections)
> 堆疊是處理「匹配」和「嵌套」結構問題的首選資料結構。當你看到需要追蹤「最近」的某個元素時，堆疊通常是好選擇。
> 可以使用雜湊表來簡化括號匹配的邏輯：`mapping = {')': '(', ']': '[', '}': '{'}`。
> **相關題目:** 22. Generate Parentheses, 32. Longest Valid Parentheses, 150. Evaluate Reverse Polish Notation

---

## 121. Best Time to Buy and Sell Stock

### 121. Best Time to Buy and Sell Stock

- **連結:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- **標籤:** `Array`, `Dynamic Programming`, `Greedy`
- **日期:** 2026-01-12

#### 1. 問題理解 (Problem Understanding)
> 給定一個陣列 `prices`，其中 `prices[i]` 是股票在第 `i` 天的價格。你想選擇某一天買入股票，並在未來的某一天賣出，以最大化利潤。返回最大利潤，若無法獲利則返回 0。
>
> **Constraints:** 陣列長度 `1 <= prices.length <= 10^5`，價格範圍 `0 <= prices[i] <= 10^4`。
> **Edge Cases:** 只有一天（無法交易）、價格持續下跌（最大利潤為 0）。

#### 2. 初步想法 & 暴力解 (Initial Thoughts & Brute-Force)
> 使用兩層迴圈，外層選擇買入日，內層選擇賣出日，計算所有可能的利潤並找最大值。
> 時間複雜度是 O(n^2)，空間複雜度是 O(1)。

```python
def maxProfit_bruteforce(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit
```

#### 3. 最優解 (Optimal Solution)
> 核心觀念是**貪心法 (Greedy)**：在遍歷過程中追蹤到目前為止的最低價格，並計算當前價格與最低價格的差值作為潛在利潤。
>
> 演算法步驟：
> 1. 初始化 `min_price` 為無限大，`max_profit` 為 0。
> 2. 遍歷每一天的價格 `price`：
>    - 更新 `min_price = min(min_price, price)`（追蹤到目前為止的最低價）。
>    - 更新 `max_profit = max(max_profit, price - min_price)`（計算若今天賣出的利潤）。
> 3. 返回 `max_profit`。

- **時間複雜度:** O(n)，只需遍歷陣列一次。
- **空間複雜度:** O(1)，只使用常數額外空間。

```python
def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
```

#### 4. 關鍵心得 & 延伸 (Key Takeaways & Connections)
> 這是一個經典的「單次遍歷追蹤狀態」問題。關鍵洞察是：要最大化利潤，我們需要在最低點買入，所以只需追蹤遍歷過程中的最低價格。
> 這也可以用動態規劃的思維來理解：`dp[i]` 代表前 i 天的最大利潤。
> **相關題目:** 122. Best Time to Buy and Sell Stock II, 123. Best Time to Buy and Sell Stock III, 309. Best Time to Buy and Sell Stock with Cooldown

---

## 26. Remove Duplicates from Sorted Array

### 26. Remove Duplicates from Sorted Array

- **連結:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- **標籤:** `Array`, `Two Pointers`
- **日期:** 2026-01-12

#### 1. 問題理解 (Problem Understanding)
> 給定一個**已排序**的整數陣列 `nums`，原地 (in-place) 移除重複的元素，使每個元素只出現一次，並返回新的長度。不需要考慮陣列中超出新長度後的元素。
>
> **Constraints:** 陣列長度 `1 <= nums.length <= 3 * 10^4`，數字範圍 `-100 <= nums[i] <= 100`，陣列已按升序排列。
> **Edge Cases:** 陣列只有一個元素、所有元素都相同、沒有重複元素。

#### 2. 初步想法 & 暴力解 (Initial Thoughts & Brute-Force)
> 可以使用額外的陣列或集合來儲存不重複的元素，但這違反了「原地」的要求。
> 由於陣列已排序，重複元素必定相鄰，這是可以利用的特性。

#### 3. 最優解 (Optimal Solution)
> 核心觀念是**雙指針 (Two Pointers)**：一個慢指針 `i` 指向要放置下一個不重複元素的位置，一個快指針 `j` 用來遍歷陣列。
>
> 演算法步驟：
> 1. 初始化慢指針 `i = 0`。
> 2. 使用快指針 `j` 從索引 1 開始遍歷陣列。
> 3. 如果 `nums[j] != nums[i]`（發現新的不重複元素）：
>    - 將 `i` 前進一步。
>    - 將 `nums[j]` 複製到 `nums[i]`。
> 4. 遍歷結束後，返回 `i + 1`（新陣列的長度）。

- **時間複雜度:** O(n)，只需遍歷陣列一次。
- **空間複雜度:** O(1)，原地修改，只使用常數額外空間。

```python
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
```

#### 4. 關鍵心得 & 延伸 (Key Takeaways & Connections)
> 雙指針技巧在處理「原地修改已排序陣列」的問題上非常有效。慢指針維護「已處理區域」的邊界，快指針負責探索新元素。
> 記住：已排序陣列中，相同的元素必定相鄰，這大大簡化了重複檢測。
> **相關題目:** 27. Remove Element, 80. Remove Duplicates from Sorted Array II, 283. Move Zeroes

