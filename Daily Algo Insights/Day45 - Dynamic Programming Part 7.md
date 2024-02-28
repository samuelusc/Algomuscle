# Day45 - Dynamic Programming Part 7

## Contents
* **[climbing Stairs](#70)**
* **[advanced climbing staris](#57)**
* **[322. Coin Change](#322)**
* **[279. Perfect Squares](#279)**
* **[Amazon warehouse distribution](#amz)**
<br>


<h2 id = "70"><a href="https://leetcode.com/problems/climbing-stairs">70. Climbing Stairs</a></h2><h3>Easy</h3><hr><p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

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
### Breakdown and Thought Process:  
<br>

### My Solution 1：_`normal`_  

  
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]

```


- *`Time Complexity`*:<br>
O(n) where n is the input number of steps
  
- *`Space Complexity`*:<br>
O(n)
---
  
### My Solution 2：_`sapce save`_  

  
```python

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * 3
        # following the fibonacci sequence pattern
        dp[1],dp[2] = 1,2
        for i in range(3,n+1):
            sum = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = sum

        return dp[2]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
o(n) where n is the input number of steps
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


### 57. 爬楼梯 <a name = "57"></a>
#### [Question Reference](https://kamacoder.com/problempage.php?pid=1067)

### 题目描述
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 

每次你可以爬至多m (1 <= m < n)个台阶。你有多少种不同的方法可以爬到楼顶呢？ 

注意：给定 n 是一个正整数。

### 输入描述
输入共一行，包含两个正整数，分别表示n, m

### 输出描述
输出一个整数，表示爬到楼顶的方法数。

### 输入示例
3 2

### 输出示例
3

### 提示信息
数据范围：

1 <= m < n <= 32;

当 m = 2，n = 3 时，n = 3 这表示一共有三个台阶，m = 2 代表你每次可以爬一个台阶或者两个台阶。

此时你有三种方法可以爬到楼顶。

1. 1 阶 + 1 阶 + 1 阶段

2. 1 阶 + 2 阶

3. 2 阶 + 1 阶



### My Solution： 

  
```python

class Solution:
    def climb_stairs(self, n , m):
        
        dp = [0] * (n + 1)
        
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(1, m + 1):
                dp[i] += dp[i-j]
        
        
        return dp[-1]
        

if __name__ == "__main__":
    n,m = [int(x) for x in input().split()]
    sol = Solution()
    
    res = sol.climb_stairs(n,m)
    
    print(res)
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n*m)
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "322"><a href="https://leetcode.com/problems/coin-change">322. Coin Change</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>


### My Solution：  

  
```python

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j-coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(S *n) where S is the amount to make change for, and n is the number of different coin denominations available.
  
- *`Space Complexity`*:<br>
O(S) where s is the amount to make change for
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "279"><a href="https://leetcode.com/problems/perfect-squares">279. Perfect Squares</a></h2><h3>Medium</h3><hr><p>Given an integer <code>n</code>, return <em>the least number of perfect square numbers that sum to</em> <code>n</code>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, <code>1</code>, <code>4</code>, <code>9</code>, and <code>16</code> are perfect squares while <code>3</code> and <code>11</code> are not.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong> 12 = 4 + 4 + 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 2
<strong>Explanation:</strong> 13 = 4 + 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>
<br>

### My Solution：_`While Dp`_  

  
```python

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)

        dp[0] = 0

        for i in range(1,n+1):
            j = 1

            while i >= j*j:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j+=1

        return dp[-1]
```


- *`Time Complexity`*:<br>
O(n*m) where m is the integer square root of n 
  
- *`Space Complexity`*:<br>
O(n)
---

### My Solution：_`For loop DP`_  

  
```python

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, int(n**0.5) + 1):
            for j in range(i*i, n+1):
                dp[j]= min(dp[j], dp[j-i*i]+1)

        return dp[-1] 
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n*m) where m is the integer square root of n 

  
- *`Space Complexity`*:<br>
O(n)

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>

### Warehouse Distribution <a name = "amz"></a>
![Warehouse Distribution](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day45/Warehouse%20Distribution.jpg)

### My Solution：_`concised`_  

  
```python

class Solution:
    def warehouse(self, nums):
        total = 0
        for num in nums:
            total += num
        avg = total // len(nums)
        less_count, great_count = 0, 0

        for num in nums:
            if num < avg:
                less_count += avg - num

            if num > avg + 1:
                great_count += num - (avg+1)

        return max(less_count, great_count)


sol = Solution()
res = sol.warehouse([1, 2, 5, 7])
print(res)
```


- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(1)
---
  

 
### My Solution 2：_`sort + 2 pointers`_  

  
```python

class Solution:
    def warehouse_distribution(self, nums):
        s_list = sorted(nums)

        left, right, count = 0, len(s_list)-1, 0

        if s_list[left] == s_list[right] or len(s_list) < 2:
            return 0

        while left < right and s_list[right] - s_list[left] > 1:

            s_list[right] -= 1
            s_list[left] += 1
            count += 1
            if s_list[left] > s_list[left + 1]:
                left += 1
            if s_list[right] < s_list[right - 1]:
                right -= 1
        print(s_list)
        return count
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(nlogn)
  
- *`Space Complexity`*:<br>
O(n) (can be O(1) in-place sort)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>
