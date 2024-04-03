# Day50 - Dynamic Programming Part 11



## Contents
* **[123. Best Time to Buy and Sell Stock III](#123)**
* **[188. Best Time to Buy and Sell Stock IV](#188)**

<br>
<h2 id = "123"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii">123. Best Time to Buy and Sell Stock III</a></h2><h3>Hard</h3><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete <strong>at most two transactions</strong>.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<br>

### Solving approach 1:


![123-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day50/LC123-thought.jpg)



### My Solution：

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # deploy DP to solve it 
        dp = [[0] * 4 for _ in range(len(prices))] 
        dp[0][0] = -prices[0] # first transaction
        dp[0][1] = 0
        dp[0][2] = -prices[0] # second transaction
        dp[0][3] = 0
        for i in range(1,len(prices)):
            # define four states 
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2] + prices[i])

        return dp[-1][3]
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n) , where n is the number of elements in prices.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of elements in prices.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




<h2 id = "188"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv">188. Best Time to Buy and Sell Stock IV</a></h2><h3>Hard</h3><p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer <code>k</code>.</p>

<p>Find the maximum profit you can achieve. You may complete at most <code>k</code> transactions: i.e. you may buy at most <code>k</code> times and sell at most <code>k</code> times.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 2, prices = [2,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 2, prices = [3,2,6,5,0,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>1 &lt;= prices.length &lt;= 1000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>



### Solving approach 1:


![188-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day50/LC188-thought.jpg)


### My Solution：

  
```python

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * (2*k + 1) for _ in range(len(prices))]

        for j in range(1, 2*k + 1, 2):
            dp[0][j] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(1, 2 * k + 1):
                if j % 2 != 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i]) 
        
        return dp[-1][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * k)
  
- *`Space Complexity`*:<br>
O(n * k)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>












