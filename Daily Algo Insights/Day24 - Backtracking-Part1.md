# Day24 - Backtracking Part 1

### [Study Reference](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)  


## Contents
* **[77. Combinations](#77)**


<br>
<h2 id = "77"><a href="https://leetcode.com/problems/combinations">77. Combinations</a></h2><h3>Medium</h3><hr><p>Given two integers <code>n</code> and <code>k</code>, return <em>all possible combinations of</em> <code>k</code> <em>numbers chosen from the range</em> <code>[1, n]</code>.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, k = 2
<strong>Output:</strong> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
<strong>Explanation:</strong> There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> [[1]]
<strong>Explanation:</strong> There is 1 choose 1 = 1 total combination.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>



### My Solution 1：_`backtracking`_  

  
```python

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, res = [], []
        def backtracking(n,k, start_index):
            if len(path) == k:
                res.append(path[:])
                return 
            

            for i in range(start_index, n - (k-len(path)) + 2):
                path.append(i)

                # 不是 start_index + 1,是当前i + 1
                backtracking(n,k, i + 1) 
                path.pop()
        
        backtracking(n,k,1)
        return res
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
O(C(n,k)×k), C(n,k)= n!/ (k!(n−k)!). paht[:] costs O(k)
  
- *`Space Complexity`*:<br>
O(C(n,k)×k), C(n,k)= n!/ (k!(n−k)!). paht[:] costs O(k)

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>










