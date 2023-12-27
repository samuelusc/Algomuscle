# Arrays Part

## Table of Content
1. [704. Binary Search](#704)
2. [27. Remove Element](#27)

## 704. Binary Search <a name='704'></a>
<a href="https://leetcode.com/problems/binary-search/description/" target="_blank">LeetCode Binary Search Problem</a>
# Binary Search in Sorted Array

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

## Example 1:

Input: `nums` = [-1,0,3,5,9,12], `target` = 9
Output: 4
Explanation: 9 exists in `nums` and its index is 4

## Example 2:

Input: `nums` = [-1,0,3,5,9,12], `target` = 2
Output: -1
Explanation: 2 does not exist in `nums` so return -1

## Constraints:

- 1 <= `nums.length` <= 104
- -104 < `nums[i]`, `target` < 104
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle

        return -1

def main():
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = solution.search(nums, target)
    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in the list")

if __name__ == "__main__":
    main()

```

