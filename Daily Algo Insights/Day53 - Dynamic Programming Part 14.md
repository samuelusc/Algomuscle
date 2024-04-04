# Day53 - Dynamic Programming Part 14


## Contents
* **[1143. Longest Common Subsequence](#1143)**
* **[1035. Uncrossed Lines](#1035)**
* **[53. Maximum Subarray](#53)**


<br>
<h2 id = "1143"><a href="https://leetcode.com/problems/longest-common-subsequence">1143. Longest Common Subsequence</a></h2><h3>Medium</h3><p>Given two strings <code>text1</code> and <code>text2</code>, return <em>the length of their longest <strong>common subsequence</strong>. </em>If there is no <strong>common subsequence</strong>, return <code>0</code>.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code>.</li>
</ul>

<p>A <strong>common subsequence</strong> of two strings is a subsequence that is common to both strings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abcde&quot;, text2 = &quot;ace&quot; 
<strong>Output:</strong> 3  
<strong>Explanation:</strong> The longest common subsequence is &quot;ace&quot; and its length is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest common subsequence is &quot;abc&quot; and its length is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;def&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no such common subsequence, so the result is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text1.length, text2.length &lt;= 1000</code></li>
	<li><code>text1</code> and <code>text2</code> consist of only lowercase English characters.</li>
</ul>


### Solving approach 1:


![1143-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day53/LC1143-th.jpg)


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)] 

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * m), where n is the length of text1 and m is the length of text2.
  
- *`Space Complexity`*:<br>
O(n * m), proportional to the dimensions of the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "1035"><a href="https://leetcode.com/problems/uncrossed-lines">1035. Uncrossed Lines</a></h2><h3>Medium</h3><p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>. We write the integers of <code>nums1</code> and <code>nums2</code> (in the order they are given) on two separate horizontal lines.</p>

<p>We may draw connecting lines: a straight line connecting two numbers <code>nums1[i]</code> and <code>nums2[j]</code> such that:</p>

<ul>
	<li><code>nums1[i] == nums2[j]</code>, and</li>
	<li>the line we draw does not intersect any other connecting (non-horizontal) line.</li>
</ul>

<p>Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).</p>

<p>Return <em>the maximum number of connecting lines we can draw in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/26/142.png" style="width: 400px; height: 286px;" />
<pre>
<strong>Input:</strong> nums1 = [1,4,2], nums2 = [1,2,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 2000</code></li>
</ul>




### Solving approach 1:


![1035-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day53/LC1035-th.jpg)



### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1,len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * m), where n is the length of nums1 and m is the length of nums2.
  
- *`Space Complexity`*:<br>
O(n * m), which is proportional to the size of the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "53"><a href="https://leetcode.com/problems/maximum-subarray">53. Maximum Subarray</a></h2><h3>Medium</h3><p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>




### Solving approach:


![53-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day53/LC53-th.jpg)



### My Solution 1：_`Kadane`_  

  
```python

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        res, count = float('-inf'),float('-inf')
        for num in nums: 
            #现在的数值是取求和，或是重新以现在的数值开始
            count = num + max(count, 0)
            
            res = max(res, count)
        
        return res
```


- *`Time Complexity`*:<br>
O(n), where n is the number of elements in nums.
  
- *`Space Complexity`*:<br>
O(1), meaning it requires constant space regardless of the input size.
---

 
### My Solution 2：_`dp`_  

  
```python

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

            if res < dp[i]:
                res = dp[i]

        return res
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of elements in nums.
  
- *`Space Complexity`*:<br>
O(n), as the size of the dp array scales linearly with the size of the input list nums.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>

