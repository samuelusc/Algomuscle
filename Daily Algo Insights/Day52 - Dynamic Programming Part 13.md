# Day52 - Dynamic Programming Part 13


## Contents
* **[300. Longest Increasing Subsequence](#300)**
* **[674. Longest Continuous Increasing Subsequence](#674)**
* **[718. Maximum Length of Repeated Subarray](#718)**


<br>
<h2 id = "300"><a href="https://leetcode.com/problems/longest-increasing-subsequence">300. Longest Increasing Subsequence</a></h2><h3>Medium</h3><p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>strictly increasing </strong></em><span data-keyword="subsequence-array"><em><strong>subsequence</strong></em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b>&nbsp;Can you come up with an algorithm that runs in&nbsp;<code>O(n log(n))</code> time complexity?</p>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![300thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day52/LC300-Th.jpg)


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
         dp = [1] * len(nums)

         for i in range(1, len(nums)):
             for j in range(i):
                 if nums[i] > nums[j]:
                     dp[i] = max(dp[j]+1,dp[i])


         return max(dp)
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n), where n is the number of elements in nums.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "674"><a href="https://leetcode.com/problems/longest-continuous-increasing-subsequence">674. Longest Continuous Increasing Subsequence</a></h2><h3>Easy</h3><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest <strong>continuous increasing subsequence</strong> (i.e. subarray)</em>. The subsequence must be <strong>strictly</strong> increasing.</p>

<p>A <strong>continuous increasing subsequence</strong> is defined by two indices <code>l</code> and <code>r</code> (<code>l &lt; r</code>) such that it is <code>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</code> and for each <code>l &lt;= i &lt; r</code>, <code>nums[i] &lt; nums[i + 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


### Solving approach:  


![674-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day52/LC674-th.jpg)

 
### My Solution：

  
```python

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # initialzation
        dp = [1] * len(nums)
        # output
        res = 1
        # iterate through the list nums
        for i in range(1,len(nums)):
            # increasing subsequemnce
            if nums[i] > nums[i-1]:
                # continuous one 
                dp[i] = dp[i-1] + 1
            # assign the longest value to the output
            if res < dp[i]:
                res = dp[i]

        return res
            
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the length of the nums list.
  
- *`Space Complexity`*:<br>
O(n), due to the dp array which scales linearly with the size of the input list nums.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = ""718><a href="https://leetcode.com/problems/maximum-length-of-repeated-subarray">718. Maximum Length of Repeated Subarray</a></h2><h3>Medium</h3><p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>the maximum length of a subarray that appears in <strong>both</strong> arrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The repeated subarray with maximum length is [3,2,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The repeated subarray with maximum length is [0,0,0,0,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>




### Solving approach:  


![718-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day52/LC718-th.jpg)


 
### My Solution：

  
```python

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1)+1)]
        res = 0

        for i in range(1,len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] ==nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                
                if res < dp[i][j]:
                    res = dp[i][j]
        return res
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * m), where n is the length of nums1 and m is the length of nums2.

  
- *`Space Complexity`*:<br>
O(n * m), which is proportional to the size of the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>





