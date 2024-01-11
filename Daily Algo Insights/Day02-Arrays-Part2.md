# Day02 - Arrays Part 2


## Contents
* **[977.Squares of a Sorted Array](#977)**
* **[209.Minimum Size Subarray Sum](#209)**
* **[54.Spiral Matrix](#54)**
* **[59.Spiral Matrix II](#59)**

<br>

![Day 2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day2/Day2.png)
<br>
<h2 id = "977"><a href="https://leetcode.com/problems/squares-of-a-sorted-array">977. Squares of a Sorted Array</a></h2><h3>Easy</h3><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?


### My Solution 1：_`xxx`_  

  
```python


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #two pointers

        left, right, end = 0, len(nums) - 1, len(nums) -1
        res = [0] * len(nums)

        # 观察知道最大数要么是最左边的平方，要么最右边的平方
        # 对新数组赋值从后往前
        while left <= right:
            if nums[left]**2 >= nums[right]**2:
                res[end] = nums[left] ** 2 
                
                end -= 1
                left += 1
            
            else:
                res[end] = nums[right] ** 2

                end -= 1
                right -= 1
        
        return res
```

**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id ="209"><a href="https://leetcode.com/problems/minimum-size-subarray-sum">209. Minimum Size Subarray Sum</a></h2><h3>Medium</h3><p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return <em>the <strong>minimal length</strong> of a </em><span data-keyword="subarray-nonempty"><em>subarray</em></span><em> whose sum is greater than or equal to</em> <code>target</code>. If there is no such subarray, return <code>0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 7, nums = [2,3,1,2,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem constraint.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 4, nums = [1,4,4]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution of which the time complexity is <code>O(n log(n))</code>.



### My Solution 1：_`two pointer`_  

  
```python

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,sum_all,max_len = 0, 0, len(nums)+1

        for right in range(len(nums)):
            sum_all += nums[right]
            
            while sum_all >= target:
                max_len = min(max_len, right - left + 1)
                sum_all -= nums[left]
                left += 1
        

        return max_len if max_len <= len(nums) else 0
```

---
  

**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id ="54"><a href="https://leetcode.com/problems/spiral-matrix">54. Spiral Matrix</a></h2><h3>Medium</h3><p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>



### My Solution 1：_`4directions`_  

  
```python

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        index, row, col = 0,0,0
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m*n):
            
            res.append(matrix[row][col])
            visited.add((row,col))

            next_row,next_col = row + directions[index][0], col + directions[index][1]
            if not 0 <= next_row < m or not 0 <= next_col < n or (next_row,next_col) in visited:
                index = (index + 1) % 4

            row += directions[index][0]
            col += directions[index][1]

        return res
```

**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "59"><a href="https://leetcode.com/problems/spiral-matrix-ii">59. Spiral Matrix II</a></h2><h3>Medium</h3><p>Given a positive integer <code>n</code>, generate an <code>n x n</code> <code>matrix</code> filled with elements from <code>1</code> to <code>n<sup>2</sup></code> in spiral order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[1,2,3],[8,9,4],[7,6,5]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
</ul>



### My Solution 1：_`4 Directions`_  

  
```python

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[n]]
        
        row, col, index = 0, 0, 0
        matrix = [[0]*n for _ in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(1,n*n+1):
            matrix[row][col] = i
                      
            x,y = directions[index]
            next_row,next_col = row + x, col + y


            if not 0<= next_row < n or not 0<= next_col <n or matrix[next_row][next_col] != 0:
                index = (index + 1) % 4

            x,y = directions[index]           
            row, col = row + x, col + y
        
        return matrix
             
        

```

---
  

### My Solution 2：_`imitation for n^2`_  

  
```python

#only work for square matrix
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        matrix = [[0] * n for _ in range(n)]
        loop, mid = n//2, n//2
        startx,starty = 0,0
        count = 1

        for offset in range(1, loop + 1):
            
            for j in range(starty, n-offset):
                matrix[startx][j] = count
                count += 1

            for i in range(startx, n-offset):
                matrix[i][n-offset] = count
                count += 1

            for j in range(n-offset, starty, -1):
                matrix[n-offset][j] = count
                count += 1

            for i in range(n-offset, startx, -1):
                matrix[i][starty] = count
                count += 1

            startx += 1
            starty += 1
        
        if n % 2 != 0:
            matrix[mid][mid] = count

        return matrix  
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



xxxx
