# Day48 - Dynamic Programming Part 10


## Contents
* **[121. Best Time to Buy and Sell Stock](#121)**
* **[best-time-to-buy-and-sell-stock-ii](#122)**

<br>

<h2 id = "121"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">121. Best Time to Buy and Sell Stock</a></h2><h3>Easy</h3><hr><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<br>

### Solving approach:


![121-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day48/LC121-thought_1.jpg)
![121-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day48/LC121-thought_2.jpg)



### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]

        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])


        return dp[-1][1]
```


- *`Time Complexity`*:<br>
O(n), where n is the length of the list prices.
  
- *`Space Complexity`*:<br>
O(n)

---

 
### My Solution 2：_`Greedy`_  

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = float("inf")

        for price in prices:
            maxi = max(maxi, price - mini)
            mini = min(price, mini)

        return maxi
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n) where n is the length of the list prices
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
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



### Solving approach:  


[122](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day48/LC122-Thought.jpg)

 
### My Solution ：_`DP`_  

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[0] * 2 for _ in range(len(prices))]

        dp[0][0] = - prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            
        return dp[-1][1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n) where n is the length of the list prices.
  
- *`Space Complexity`*:<br>
O(n)
---
 
### My Solution 2：_`Greedy`_  

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        count = 0
        for i in range(len(prices) -1):
            count = count + max(prices[i+1] - prices[i], 0)

        return count 
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n) whre n is the length of the prices list
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


