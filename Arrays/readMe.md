# Arrays Part

## Table of Content
1. [704. Binary Search](#704)
2. [27. Remove Element](#27)

## 704. Binary Search <a name='704'></a>
<a href="https://leetcode.com/problems/binary-search/description/" target="_blank">704. Binary Search</a>

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

### Example 1:

Input: `nums` = [-1,0,3,5,9,12], `target` = 9
Output: 4
Explanation: 9 exists in `nums` and its index is 4

### Example 2:

Input: `nums` = [-1,0,3,5,9,12], `target` = 2
Output: -1
Explanation: 2 does not exist in `nums` so return -1

### Constraints:

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


## 27. Remove Element <a name="27"></a>
<a href="https://leetcode.com/problems/remove-element/description/" target="_blank">27.Remove Element</a>

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

**To Get Accepted:**

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

<pre>
int[] nums = [...]; // Input array
int val = ...;     // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>


### Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

### Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

### Constraints:

- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100


```python
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for num in nums:
            if num != val:
                nums[slow] = num
                slow += 1
        return slow

def main():
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print("Test case 1 - Original List: {}, Value to Remove: {}".format(nums1, val1))
    new_length1 = solution.removeElement(nums1, val1)
    print("New length:", new_length1)
    print("Modified List:", nums1[:new_length1]) 

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print("\nTest case 2 - Original List: {}, Value to Remove: {}".format(nums2, val2))
    new_length2 = solution.removeElement(nums2, val2)
    print("New length:", new_length2)
    print("Modified List:", nums2[:new_length2]) 


if __name__ == "__main__":
    main()
```
