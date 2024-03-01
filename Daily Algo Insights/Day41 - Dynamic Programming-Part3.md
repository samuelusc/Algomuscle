
# Day41 - Dynamic Programming Part 3


## Contents
* **[343. Integer Break](#343)**
* **[96. Unique Binary Search Trees](#96)**

<br>

<h2 id = "343"><a href="https://leetcode.com/problems/integer-break">343. Integer Break</a></h2><h3>Medium</h3><hr><p>Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 &times; 1 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>



### Solving approach:


[343-thought1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day41/Leetcode343-thought.jpg)




### My Solution：

  
```python

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        dp = [0] * (n + 1)
        dp[2] = 1
         
        for i in range(3, n+1):
            for j in range(1, i//2 + 1):
                dp[i] = max(j * (i-j), j * dp[i-j], dp[i])

        return dp[-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "96"><a href="https://leetcode.com/problems/unique-binary-search-trees">96. Unique Binary Search Trees</a></h2><h3>Medium</h3><hr><p>Given an integer <code>n</code>, return <em>the number of structurally unique <strong>BST&#39;</strong>s (binary search trees) which has exactly </em><code>n</code><em> nodes of unique values from</em> <code>1</code> <em>to</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 19</code></li>
</ul>



### Solving approach:  


[96-thought1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day41/Leetcode96-thought_1.jpg)
[96-thought2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day41/Leetcode96-thought_2.jpg)

 
### My Solution：

  
```python

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)

        dp[0] = 1

        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]


        
        return dp[-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2), where n is the given input
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




