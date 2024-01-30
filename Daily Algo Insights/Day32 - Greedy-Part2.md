# Day32 - Greedy Part2


## Contents
* **[122. Best Time to Buy and Sell Stock II](#122)**
* **[55. Jump Game](#55)**
* **[45. Jump Game II](#45)**
* **[Jump Game](#MS)**



<br>
<h2 id = "122"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii">122. Best Time to Buy and Sell Stock II</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>On each day, you may decide to buy and/or sell the stock. You can only hold <strong>at most one</strong> share of the stock at any time. However, you can buy it then immediately sell it on the <strong>same day</strong>.</p>

<p>Find and return <em>the <strong>maximum</strong> profit you can achieve</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<br>

### Solving approach 1:


xxxx


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        count = 0
        for i in range(len(prices) -1):
            count = count + max(prices[i+1] - prices[i], 0)

        return count 
```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "55"><a href="https://leetcode.com/problems/jump-game">55. Jump Game</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>. You are initially positioned at the array&#39;s <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>

<p>Return <code>true</code><em> if you can reach the last index, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>




### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cover = 0

        for index, jump in enumerate(nums):
            # if max cover cannot reach index
            # just return False

            if cover < index:
                return False

            # pick up the longest cover jump
            cover = max(cover, index + jump)

        #never meet the case of False
        return True
```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




<h2 id = "45"><a href="https://leetcode.com/problems/jump-game-ii">45. Jump Game II</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>. You are initially positioned at <code>nums[0]</code>.</p>

<p>Each element <code>nums[i]</code> represents the maximum length of a forward jump from index <code>i</code>. In other words, if you are at <code>nums[i]</code>, you can jump to any <code>nums[i + j]</code> where:</p>

<ul>
	<li><code>0 &lt;= j &lt;= nums[i]</code> and</li>
	<li><code>i + j &lt; n</code></li>
</ul>

<p>Return <em>the minimum number of jumps to reach </em><code>nums[n - 1]</code>. The test cases are generated such that you can reach <code>nums[n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>It&#39;s guaranteed that you can reach <code>nums[n - 1]</code>.</li>
</ul>






### My Solution 1：_`xxx`_  

  
```python


```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



<h2 id = "MS">Jump Game - MicroSoft</h2>

*You are given an array of non-negative integers arr and a start index. When you are at an index i, you can move left or right by arr[i]. Your task is to figure out if you can reach value 0.*

`Example 1:`

Input: arr = [3, 4, 2, 3, 0, 3, 1, 2, 1], start = 7

Output: true

Explanation:
left -> left -> right


`Example 2:`

Input: arr = [3, 2, 1, 3, 0, 3, 1, 2, 1], start = 2

Output: false


### My Solution 1：_`Greedy-queue`_  
```python
from typing import List
from collections import deque
def jump_game(arr: List[int], start: int) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    visited = set()
    queue = deque([start])
    
    while queue:
        size = len(queue)
        
        for i in range(size):
            cur_index = queue.popleft()
            if cur_index in visited:
                continue
            visited.add(cur_index)
            
            if arr[cur_index] == 0:
                return True
            
            if cur_index + arr[cur_index] < len(arr):
                queue.append(cur_index + arr[cur_index])
            if cur_index - arr[cur_index] >= 0:
                queue.append(cur_index - arr[cur_index])
                
    return False

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    start = int(input())
    res = jump_game(arr, start)
    print('true' if res else 'false')
```
