# Day38 - Dynamic Programming Part 1.md


## Contents
* **[509. Fibonacci Number](#509)**
* **[70. Climbing Stairs](#70)**
* **[746. Min Cost Climbing Stairs](#746)**

<br>


### Fundamental Points:  
![DP fundamental points](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day38/The%20foundation%20of%20DP.jpg)<br>



<h2><a href="https://leetcode.com/problems/fibonacci-number">509. Fibonacci Number</a></h2><h3>Easy</h3><hr><p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>



### Solving approach 1:


![509 thought process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day38/Leetcode509-thought.jpg)<br>



 
### My Solution 2：_`save space - dp`_  

  
```python

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        

        dp = [0] * (n+1)
        dp[0],dp[1] = 0,1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the size of the input
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2><a href="https://leetcode.com/problems/climbing-stairs">70. Climbing Stairs</a></h2><h3>Easy</h3><hr><p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>



### Solving approach 2:  


![70 thought process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day38/Leetcode70-thought.jpg)<br>



### My Solution 2：_`xxx`_  

  
```python

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        first,second = 1, 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return third
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2><a href="https://leetcode.com/problems/min-cost-climbing-stairs">746. Min Cost Climbing Stairs</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.</p>

<p>You can either start from the step with index <code>0</code>, or the step with index <code>1</code>.</p>

<p>Return <em>the minimum cost to reach the top of the floor</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> cost = [10,<u>15</u>,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= cost.length &lt;= 1000</code></li>
	<li><code>0 &lt;= cost[i] &lt;= 999</code></li>
</ul>




### Solving approach 2:  


[746 thought process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day38/Leetcode746-thought.jpg.jpg)




### My Solution 2：_`save space dp`_  

  
```python

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 这里必须 + 1
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx


















