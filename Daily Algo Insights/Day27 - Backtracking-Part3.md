# Day27 - Backtracking Part3.md


## Contents
* **[39.Combination Sum](#39)**
* **[40. Combination Sum II](#40)**
* **[131.Palindrome Partitioning](#131)**


<br>
<h2 id ="39"><a href="https://leetcode.com/problems/combination-sum">39. Combination Sum</a></h2><h3>Medium</h3><p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the <span data-keyword="frequency-array">frequency</span> of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>


### My Solution 1：_`backtracking + pruning`_  

  
```python

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtracking(candidates, target, current_sum, startIndex):

            if current_sum == target:
                res.append(path[:])
                return

            for i in range(startIndex, len(candidates)):
                current_sum += candidates[i]
                if current_sum > target: 
                    break

                path.append(candidates[i])
                # 注意这里是i, 因为元素可以重复使用
                backtracking(candidates, target, current_sum, i)
                
                # sum 减去最后的candidate
                current_sum -= candidates[i]
                path.pop()

        backtracking(candidates, target, 0, 0) 

        return res
        



               

```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^k) where n is the number of candidates and k is the maximum recursion depth,
- *`Space Complexity`*:<br>
O(n^k)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "40"><a href="https://leetcode.com/problems/combination-sum-ii">40. Combination Sum II</a></h2><h3>Medium</h3><p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>







### My Solution 1：_`backtracking`_  

  
```python

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序让相邻元素在一起
        # 树层去重，树枝不去重

        candidates.sort()
        res = []
        path = []

        def backtracking(candidates, target, current_sum, startIndex):
            if current_sum == target:
                res.append(path[:])

            
            for i in range(startIndex, len(candidates)):
                #检查相邻的两个是否相等
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue

                # pruning branches
                if current_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                # 传递新的 current_sum,
                # 这样backtracking 就不需要 current_sum - candidates[i]
                backtracking(candidates, target, current_sum + candidates[i], i + 1)
                path.pop()

        backtracking(candidates, target, 0, 0)

        return res

       
```




**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(2^n), where n is the number of elements in candidates.   
- *`Space Complexity`*:<br>
 O(2^n), where n is the number of elements in candidates.

<br>




<h2 id = "131"><a href="https://leetcode.com/problems/palindrome-partitioning">131. Palindrome Partitioning</a></h2><h3>Medium</h3><p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string"><strong>palindrome</strong></span>. Return <em>all possible palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
### Breakdown and Thought Process:  
<br>


### My Solution 1：_`backtracking + revisedComparation`_  

  
```python

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        path = []
        

        def backtracking(str, startIndex):
            if startIndex == len(str):
                res.append(path[:])
                return

            for i in range(startIndex, len(s)):
                check_s = s[startIndex : i+1]
                if check_s == check_s[::-1]:
                    path.append(check_s)

                else:
                    continue

                backtracking(s, i + 1)
                path.pop()
            
        backtracking(s,0)
        return res
        



               

```

  
### Solving approach 2:  


可以建立回文动态规划表，建立需要O(n^2) 但是查询变成O(1)

这个表可以通过以下方式填充：

对于所有单字符子串，dp[i][i] = True（因为单个字符总是回文）。

对于长度为 2 的子串，dp[i][i+1] = (s[i] == s[i+1])。

对于更长的子串，dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]。

填充这个表需要 O(N^2) 的时间和空间，其中 N 是字符串的长度。

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(N^2 * 2^N) where N is the string of length.
  
- *`Space Complexity`*:<br>
O(N^2 * 2^N) where N is the string of length.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


