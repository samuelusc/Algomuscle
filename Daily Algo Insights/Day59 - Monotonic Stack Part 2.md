# Day59 - Monotonic Stack Part 2


## Contents
* **[503. Next Greater Element II](#503)**
* **[42. Trapping Rain Water](#42)**

<br>
<h2 id = "503"><a href="https://leetcode.com/problems/next-greater-element-ii">503. Next Greater Element II</a></h2><h3>Medium</h3><p>Given a circular integer array <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return <em>the <strong>next greater number</strong> for every element in</em> <code>nums</code>.</p>

<p>The <strong>next greater number</strong> of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn&#39;t exist, return <code>-1</code> for this number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [2,-1,2]
Explanation: The first 1&#39;s next greater number is 2; 
The number 2 can&#39;t find next greater number. 
The second 1&#39;s next greater number needs to search circularly, which is also 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,3]
<strong>Output:</strong> [2,3,4,-1,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![503-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day59/LC503-th.jpg)


### My Solution 1：_`Modulo`_  

  
```python

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]

        for i in range(1, len(nums) * 2):
            index = i % len(nums)

            while stack and nums[index] > nums[stack[-1]]:
                res[stack[-1]] = nums[index]
                stack.pop()
            
            stack.append(index)
        
        return res
```


- *`Time Complexity`*:<br>
O(n), where n is the length of nums.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of elements in nums.
---
  
 
### My Solution 2：_`newArray`_  

  
```python

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums1 = nums + nums
        res = [-1] * len(nums1)

        stack = [0]

        for i in range(1,len(nums1)):
            while stack and nums1[i] > nums1[stack[-1]]:
                res[stack[-1]] = nums1[i]
                stack.pop()
            
            stack.append(i)
        
        res = res[:len(nums)]
        return res


            
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "42"><a href="https://leetcode.com/problems/trapping-rain-water">42. Trapping Rain Water</a></h2><h3>Hard</h3><p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" />
<pre>
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>



### My Solution：

  
```python

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        we will use double pointer approach
        """
        # initialize the left maxium height and right maxium height
        l_max, r_max = 0,0
        
        left, right = 0, len(height)-1
        res = 0

        while left < right:
            l_max = max(l_max,height[left])
            r_max = max(r_max,height[right])

            if l_max < r_max:
                res += l_max-height[left]
                left += 1
            else:
                res += r_max-height[right]
                right -=1

        return res        
                
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the length of the height array.
  
- *`Space Complexity`*:<br>
O(1), as it only requires a constant amount of space beyond the input array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




