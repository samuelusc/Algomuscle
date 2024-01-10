# Day01 - Arrays Part 1



## Contents
* **[74.Binary Search](#704)**
* **[27.Remove Element](#27)**

<br>

![Day 1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day1/Day1.png)
<br>


<h2 id = "704"><a href="https://leetcode.com/problems/binary-search">704. Binary Search</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt; nums[i], target &lt; 10<sup>4</sup></code></li>
	<li>All the integers in <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>
### Breakdown and Thought Process:  
<br>


### My Solution 1：_`exclude right side`_  

  
```python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left is included and right is excluded

        left, right = 0, len(nums)
        # 保持循环不变量
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                # Notice here it's not mid - 1
                right = mid 

            else:
                return mid

        return -1  
                
```

---

### My Solution 2：_`include right side`_  

  
```python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left is included and right is include

        left, right = 0, len(nums) - 1
        
        # 保持循环不变量
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                # 闭空间 -1
                right = mid - 1 

            else:
                return mid

        return -1  
                
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(logn)
  
- *`Space Complexity`*:
O(1)
<br>

![Diving Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "27"><a href="https://leetcode.com/problems/remove-element">27. Remove Element</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>. The order of the elements may be changed. Then return <em>the number of elements in </em><code>nums</code><em> which are not equal to </em><code>val</code>.</p>

<p>Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i &lt; actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>



### My Solution 1：_`two Pointer`_  

  
```python

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```


- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(1)
---

 
### My Solution 2：_`brute Force`_  

  
```python

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force
        len_nums = len(nums)
        i = 0
        # 这里要用while 而不是for
        while (i < len_nums):
            if nums[i] == val:               
                for j in range(i,len_nums - 1):
                    nums[j] = nums[j+1]               
                len_nums -= 1
            # 需要重新检查移动过来的i
            else:
                i += 1

        return len_nums
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n^2)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



