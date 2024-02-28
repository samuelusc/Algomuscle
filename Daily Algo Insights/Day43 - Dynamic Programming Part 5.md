# Day43 - Dynamic Programming Part 5

## Contents
* **[1049. Last Stone Weight II](#1049)**
* **[494. Target Sum](#494)**
* **[474. Ones and Zeroes](#474)**

<br>


<h2 id = "1049"><a href="https://leetcode.com/problems/last-stone-weight-ii">1049. Last Stone Weight II</a></h2><h3>Medium</h3><p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i<sup>th</sup></code> stone.</p>

<p>We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>. The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are destroyed, and</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has new weight <code>y - x</code>.</li>
</ul>

<p>At the end of the game, there is <strong>at most one</strong> stone left.</p>

<p>Return <em>the smallest possible weight of the left stone</em>. If there are no stones left, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that&#39;s the optimal value.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [31,26,33,21,40]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 100</code></li>
</ul>
### Breakdown and Thought Process:  
<br>

## Solving approach:


![1049-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/Leetcode1049-thought.jpg)

### My Solution：_`1D`_  

  
```python

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        target = sum(stones) // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)

        res = sum(stones) - 2 * dp[target]

        return res
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n)

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "494"><a href="https://leetcode.com/problems/target-sum">494. Target Sum</a></h2><h3>Medium</h3><p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>You want to build an <strong>expression</strong> out of nums by adding one of the symbols <code>&#39;+&#39;</code> and <code>&#39;-&#39;</code> before each integer in nums and then concatenate all the integers.</p>

<ul>
	<li>For example, if <code>nums = [2, 1]</code>, you can add a <code>&#39;+&#39;</code> before <code>2</code> and a <code>&#39;-&#39;</code> before <code>1</code> and concatenate them to build the expression <code>&quot;+2-1&quot;</code>.</li>
</ul>

<p>Return the number of different <strong>expressions</strong> that you can build, which evaluates to <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], target = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 1000</code></li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
</ul>

## Solving approach:

![494-thought-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/Leetcode494-thought_1.jpg)
![494-thought-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/Leetcode494-thought_2.jpg)



### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        size = (total + target) // 2

        if abs(total) < abs(target) or (total + target) % 2 != 0:
            return 0

        dp = [0] * (size + 1)
        
        # Base case: one way to sum to 0 (using no numbers)
        dp[0] = 1 

        for num in nums:
            for j in range(size, num - 1, -1):          
                dp[j] += dp[j-num]
        

        return dp[-1]
```


- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n)
---
  
### Solving approach:  


![494-2D-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/leetcode494-2D_1.jpg)
![494-2D-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/leetcode494-2D_1.jpg)


 
### My Solution 2：_`xxx`_  

  
```python

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if total < abs(target) or ((total + target) % 2 != 0):
            return 0

        bag_size = (total + target)//2
        dp = [[0]*(bag_size+1) for _ in range(len(nums))]

        dp[0][0] = 2 if nums[0] == 0 else 1
        for j in range(1, bag_size+1):
            if nums[0] == j:
                dp[0][j] = 1

        for i in range(1, len(nums)):
            for j in range(0, bag_size+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "474"><a href="https://leetcode.com/problems/ones-and-zeroes">474. Ones and Zeroes</a></h2><h3>Medium</h3><p>You are given an array of binary strings <code>strs</code> and two integers <code>m</code> and <code>n</code>.</p>

<p>Return <em>the size of the largest subset of <code>strs</code> such that there are <strong>at most</strong> </em><code>m</code><em> </em><code>0</code><em>&#39;s and </em><code>n</code><em> </em><code>1</code><em>&#39;s in the subset</em>.</p>

<p>A set <code>x</code> is a <strong>subset</strong> of a set <code>y</code> if all elements of <code>x</code> are also elements of <code>y</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;10&quot;,&quot;0001&quot;,&quot;111001&quot;,&quot;1&quot;,&quot;0&quot;], m = 5, n = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The largest subset with at most 5 0&#39;s and 3 1&#39;s is {&quot;10&quot;, &quot;0001&quot;, &quot;1&quot;, &quot;0&quot;}, so the answer is 4.
Other valid but smaller subsets include {&quot;0001&quot;, &quot;1&quot;} and {&quot;10&quot;, &quot;1&quot;, &quot;0&quot;}.
{&quot;111001&quot;} is an invalid subset because it contains 4 1&#39;s, greater than the maximum of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;10&quot;,&quot;0&quot;,&quot;1&quot;], m = 1, n = 1
<strong>Output:</strong> 2
<b>Explanation:</b> The largest subset is {&quot;0&quot;, &quot;1&quot;}, so the answer is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 600</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists only of digits <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>


## Solving approach:  


![474-1D-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/Leetcode474-thought_1.jpg)
![474-1D-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day43/Leetcode474-thought_2.jpg)



 
### My Solution：_`1D`_  

  
```python

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # initialization
        dp = [[0] * (n+1) for _ in range(m+1)]

        for char in strs:
            # count the number of '1' and '0'
            zeros = char.count('0')
            ones = char.count('1')

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):

                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        
        return dp[m][n]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(L * (S + m * n))
1. L: This is the number of strings in the list strs.
2. S: This represents the maximum length of any string in the list strs.
3. m and n: These are not the sizes of 0's and 1's,
  
- *`Space Complexity`*:<br>
O(m * n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



