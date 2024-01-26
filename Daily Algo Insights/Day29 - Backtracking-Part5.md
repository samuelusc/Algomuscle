# Day29 - Backtracking Part 5


## Contents
* **[491. Non-decreasing Subsequences](#491)**
* **[46. Permutations](#46)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
<br>
xxximagexxx
<br>
<h2 id = "491"><a href="https://leetcode.com/problems/non-decreasing-subsequences">491. Non-decreasing Subsequences</a></h2><h3>Medium</h3><p>Given an integer array <code>nums</code>, return <em>all the different possible non-decreasing subsequences of the given array with at least two elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,6,7,7]
<strong>Output:</strong> [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,4,3,2,1]
<strong>Output:</strong> [[4,4]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 15</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>



### Solving approach 1:


xxxx


### My Solution 1：_`backtracking + set`_  

  
```python

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, startIndex):
            # 这里是开始记录的条件，而不是递归结束条件
            if len(path) > 1:
                #结果在树枝和树叶
                res.append(path[:])
            # 为什么没有加return 因为会跳过后面的元素，而这里并非截止点

            seen = set()

            for i in range(startIndex, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in seen:
                    continue
                seen.add(nums[i])
                path.append(nums[i])

                backtracking(nums, i + 1)    
                path.pop()


        backtracking(nums, 0)     
        return res
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "46"><a href="https://leetcode.com/problems/permutations">46. Permutations</a></h2><h3>Medium</h3><p>Given an array <code>nums</code> of distinct integers, return <em>all the possible permutations</em>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>



### Solving approach 1:


xxxx


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 与combination question 不同在于树枝可以重复选取
        res = []
        path = []
        visited = [False] * len(nums)

        # 这里不用startIndex,因为可以重复选取
        # 只需要避免这次已经选过的即可
        def backtracking(nums,visited):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])

                backtracking(nums,visited)
                visited[i] = False
                path.pop()


        backtracking(nums,visited)
        return res
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "47"><a href="https://leetcode.com/problems/permutations-ii">47. Permutations II</a></h2><h3>Medium</h3><p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>



### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        res = []
        visited = [False] * len(nums)
        nums.sort()
        def backtracking(nums, visited):
            if len(path) == len(nums):
                print(path)
                res.append(path[:])
                return 


            for i in range(0, len(nums)):
                # 去重逻辑1，树枝去重 3个条件
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                # 去重逻辑2，树叶去重            
                if visited[i]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtracking(nums, visited)
                visited[i] = False
                path.pop()

        backtracking(nums, visited)
        return res
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


