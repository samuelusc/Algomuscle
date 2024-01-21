# Day25  Backtracking Part 2


## Contents
* **[216.Combination Sum III](#216)**
* **[17.Letter Combinations of a Phone Number](#17)**


<br>
<h2><a href="https://leetcode.com/problems/combination-sum-iii">216. Combination Sum III</a></h2><h3>Medium</h3><hr><p>Find all valid combinations of <code>k</code> numbers that sum up to <code>n</code> such that the following conditions are true:</p>

<ul>
	<li>Only numbers <code>1</code> through <code>9</code> are used.</li>
	<li>Each number is used <strong>at most once</strong>.</li>
</ul>

<p>Return <em>a list of all possible valid combinations</em>. The list must not contain the same combination twice, and the combinations may be returned in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 7
<strong>Output:</strong> [[1,2,4]]
<strong>Explanation:</strong>
1 + 2 + 4 = 7
There are no other valid combinations.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 3, n = 9
<strong>Output:</strong> [[1,2,6],[1,3,5],[2,3,4]]
<strong>Explanation:</strong>
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 4, n = 1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 &gt; 1, there are no valid combination.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>
<br>


### My Solution 1：_`standard backtracking`_  

  
```python

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path = []
        self.res = []

        self.backtracking(k,n,0,1)
        return self.res
        
    def backtracking(self, k,n, sumAll, startIndex):
        if len(self.path) == k:
            if sumAll == n:
                self.res.append(self.path[:])
            #只要元素到达k，无论是否n都停止继续递归
            return 
        


        for i in range(startIndex, 10):
            sumAll += i
            # 减枝 prune invalid if samAll > n
            if sumAll > n:
                continue
            self.path.append(i)

            self.backtracking(k,n,sumAll, i + 1)

            sumAll -= i
            self.path.pop()
            
```

### My Solution 2：_`prune backtracking`_  

  
```python

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path = []
        self.res = []

        self.backtracking(k,n,0,1)
        return self.res
        
    def backtracking(self, k,n, sumAll, startIndex):
        if len(self.path) == k:
            if sumAll == n:
                self.res.append(self.path[:])
            #只要元素到达k，无论是否n都停止继续递归
            return 
        
        # basic : for i in range(startIndex, 10):
        # 再减枝 如k = 6, 当i=5 时已经无效 

        for i in range(startIndex, 11 - (k-len(self.path))):
            sumAll += i
            # 减枝 prune invalid if samAll > n
            if sumAll > n:
                continue
            self.path.append(i)

            self.backtracking(k,n,sumAll, i + 1)

            sumAll -= i
            self.path.pop()
            
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(C(9,k)×k)
  
- *`Space Complexity`*:<br>
O(C(9,k)×k)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number">17. Letter Combinations of a Phone Number</a></h2><h3>Medium</h3><hr><p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png" style="width: 300px; height: 243px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;,&quot;ae&quot;,&quot;af&quot;,&quot;bd&quot;,&quot;be&quot;,&quot;bf&quot;,&quot;cd&quot;,&quot;ce&quot;,&quot;cf&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;&quot;
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;2&quot;
<strong>Output:</strong> [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>[&#39;2&#39;, &#39;9&#39;]</code>.</li>
</ul>




### My Solution 1：_`backtracking`_  

  
```python

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        combo = '' # 套函数如果需要修改要么1.作为参数传递 2. 用nonlocal 字段在套函数内声明
        if not digits:
            return []

        def backtracking(combo, index):
            
            
            # base case 终止条件
            if index == len(digits):
                result.append(combo)
                return
            
            digit = int(digits[index] )
            letters = letterMap[digit]

            for char in letters:

                backtracking(combo + char, index + 1) # 这里实现了回溯
                # combo = combo[:-1] 这部分导致错误，每次调用会产生新的combo副本
        # 先定义后调用
        backtracking(combo, 0)
        return result
            


            
```


- *`Time Complexity`*:<br>
O(4^n×n), where n is the length of digits
  
- *`Space Complexity`*:<br>
O(4^d×d), where d is the length of digits  

---
  

### My Solution 2：_`xxx`_  

  
```python

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 先映射进一个列表, 不包括 0，1
        letterMap = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]


        # 如果digits is ""
        if not digits:
            return []
        
        # 最终返回表
        res = ['']

        for digit in digits:
            #! 最开始写成了 digits 错误
            letters = letterMap[int(digit) -2 ]
            # first iteration res = ["a","b""c"] if digits = "23"
            res = [prefix + char for prefix in res for char in letters]

        return res
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(4^n), where n is the length of digits
  
- *`Space Complexity`*:<br>
O(4^n), where n is the length of digits
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




