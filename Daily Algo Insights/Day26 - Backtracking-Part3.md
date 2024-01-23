# Day26 - Backtracking Part3.md


## Contents
* **[131.Palindrome Partitioning](#131)**
* **[93.Restore IP Addresses](#93)**
* **[78.Subsets](#78)**

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


<h2 id = "93"><a href="https://leetcode.com/problems/restore-ip-addresses">93. Restore IP Addresses</a></h2><h3>Medium</h3><p>A <strong>valid IP address</strong> consists of exactly four integers separated by single dots. Each integer is between <code>0</code> and <code>255</code> (<strong>inclusive</strong>) and cannot have leading zeros.</p>

<ul>
	<li>For example, <code>&quot;0.1.2.201&quot;</code> and <code>&quot;192.168.1.1&quot;</code> are <strong>valid</strong> IP addresses, but <code>&quot;0.011.255.245&quot;</code>, <code>&quot;192.168.1.312&quot;</code> and <code>&quot;192.168@1.1&quot;</code> are <strong>invalid</strong> IP addresses.</li>
</ul>

<p>Given a string <code>s</code> containing only digits, return <em>all possible valid IP addresses that can be formed by inserting dots into </em><code>s</code>. You are <strong>not</strong> allowed to reorder or remove any digits in <code>s</code>. You may return the valid IP addresses in <strong>any</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;25525511135&quot;
<strong>Output:</strong> [&quot;255.255.11.135&quot;,&quot;255.255.111.35&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0000&quot;
<strong>Output:</strong> [&quot;0.0.0.0&quot;]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;101023&quot;
<strong>Output:</strong> [&quot;1.0.10.23&quot;,&quot;1.0.102.3&quot;,&quot;10.1.0.23&quot;,&quot;10.10.2.3&quot;,&quot;101.0.2.3&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> consists of digits only.</li>
</ul>







### My Solution 1：_`backtracking`_  

  
```python

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtracking(startIndex):
            if startIndex >= len(s) and len(path)==4:
                res.append(".".join(path))
                return

            if len(path) > 4:
                return

            for i in range(startIndex, min(startIndex + 3, len(s))):
                if is_valid (startIndex, i):
                    path.append(s[startIndex: i + 1])
                    backtracking(i + 1)
                    path.pop()


        def is_valid(start, end):
            if s[start] == "0" and end!=start :
                return False
            
            return 0 <=int(s[start: end + 1]) <= 255

        
        backtracking(0)
        return res

       
```




**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(1) in terms of input string length N, since the size of the input is not a factor beyond a certain length (the length must be between 4 and 12 for a valid IP address).
  
- *`Space Complexity`*:<br>
O(1) , as the space used does not grow significantly with the length of the input string N.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




<h2 id = "78"><a href="https://leetcode.com/problems/subsets">78. Subsets</a></h2><h3>Medium</h3><p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>






### My Solution 1：_`backtracking`_  

  
```python

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []

        self.backtracking(nums, 0)
        return self.res



    def backtracking(self, nums, startIndex):
        
        # 如果最后递归为[1,2,3]，所以先放入再检查
        self.res.append(self.path[:])

        # 下面可以省略，因为 for循环已经帮助处理 startIndex > len(nums)
        # if startIndex >= len(nums):
        #     return
    

        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(2^n).Each number has two possibilities: either it is part of a subset or it is not.
  
- *`Space Complexity`*:<br>
O(n) if we only consider auxiliary space not the space for the output. 
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


