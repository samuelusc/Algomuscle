# Day51 - Dynamic Programming Part 12


## Contents
* **[309. Best Time to Buy and Sell Stock with Cooldown](#309)**
* **[714. Best Time to Buy and Sell Stock with Transaction Fee](#714)**


<br>
<h2 id = "309"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown">309. Best Time to Buy and Sell Stock with Cooldown</a></h2><h3>Medium</h3><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:</p>

<ul>
	<li>After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).</li>
</ul>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,0,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> transactions = [buy, sell, cooldown, buy, sell]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>

<br>

### Solving approach :


[309-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day51/LC309-Thought.jpg)


### My Solution ：

  
```python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 4 for _ in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i],dp[i-1][1] - prices[i])

            dp[i][1] = max(dp[i-1][1], dp[i-1][2])

            dp[i][2] = dp[i-1][3]

            dp[i][3] = dp[i-1][0] + prices[i]
            # print(f"i is {i} and dp[{i}][3] is {dp[i][3]}")

        return max(dp[-1][1], dp[-1][2], dp[-1][3])
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of elements in prices.

  
- *`Space Complexity`*:<br>
O(n), where n is the number of elements in prices.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "714"><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee">714. Best Time to Buy and Sell Stock with Transaction Fee</a></h2><h3>Medium</h3><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer <code>fee</code> representing a transaction fee.</p>

<p>Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</li>
	<li>The transaction fee is only charged once for each stock purchase and sale.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,3,2,8,4,9], fee = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,3,7,5,10,3], fee = 3
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt; 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= fee &lt; 5 * 10<sup>4</sup></code></li>
</ul>



### Solving approach 1:


[714-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day51/LC714-Thought.jpg)



### My Solution 1：

  
```python

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]

        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]- prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

        return dp[-1][1]
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of elements in prices.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of elements in prices
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>








