# Day39 - Dynamic Programming Part 2


## Contents
* **[62. Unique Paths](#62)**
* **[63. Unique Paths II](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
<br>

<h2 id = "62"><a href="https://leetcode.com/problems/unique-paths">62. Unique Paths</a></h2><h3>Medium</h3><p>There is a robot on an <code>m x n</code> grid. The robot is initially located at the <strong>top-left corner</strong> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>Given the two integers <code>m</code> and <code>n</code>, return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The test cases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" />
<pre>
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>




### Solving approach:


![62 thought process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day39/Leetcode62-thought.jpg)





 
### My Solution：

  
```python

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range (m)]

        # not (1,m) 考虑 m = 1, n = 1, output = 1
        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1,n):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(m*n), where m is the number of rows and n is the number of columns.
  
- *`Space Complexity`*:<br>
O(m * n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "63"><a href="https://leetcode.com/problems/unique-paths-ii">63. Unique Paths II</a></h2><h3>Medium</h3><p>You are given an <code>m x n</code> integer array <code>grid</code>. There is a robot initially located at the <b>top-left corner</b> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>An obstacle and space are marked as <code>1</code> or <code>0</code> respectively in <code>grid</code>. A path that the robot takes cannot include <strong>any</strong> square that is an obstacle.</p>

<p>Return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The testcases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,1],[0,0]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == obstacleGrid.length</code></li>
	<li><code>n == obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>







### Solving approach:  


![63 thought process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day39/Leetcode63-thought.jpg)


 
### My Solution：

  
```python

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # exception check
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0 

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(m * n)
  
- *`Space Complexity`*:<br>
O(m * n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>







