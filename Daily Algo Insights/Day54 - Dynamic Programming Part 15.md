# Day54 - Dynamic Programming Part 15


## Contents
* **[392. Is Subsequence](#392)**
* **[115. Distinct Subsequences](#115)**


<br>
<h2 id = "392"><a href="https://leetcode.com/problems/is-subsequence">392. Is Subsequence</a></h2><h3>Easy</h3><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>subsequence</strong> of </em><code>t</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Suppose there are lots of incoming <code>s</code>, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![392-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day54/LC392-th_1.jpg)
![392-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day54/LC392-th_2.jpg)



### My Solution 1：_`DP`_  

  
```python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1] == len(s)
```


- *`Time Complexity`*:<br>
O(n * m), where n is the length of s and m is the length of t.
  
- *`Space Complexity`*:<br>
O(n * m), proportional to the size of the dp array.
---

### My Solution 2：_`For`_  

  
```python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_pointer = 0
        if len(s) > len(t):
            return False
        
        if not s:
            return True
        
        for char in t:
            if s[s_pointer] == char:
                s_pointer += 1

            if s_pointer == len(s):
                return True
        
        return False
```


- *`Time Complexity`*:<br>
O(m), where m is the length of t.
  
- *`Space Complexity`*:<br>
O(1), meaning it requires constant space regardless of the input size.
---

 
### My Solution 3：_`While`_  

  
```python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0

        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1

            t_pointer += 1

        return s_pointer == len(s)
            
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(m), where m is the length of t. This is because, in the worst case, the code iterates through each character of t once.
  
- *`Space Complexity`*:<br>
O(1), as it requires a constant amount of additional space regardless of the input size.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "115"><a href="https://leetcode.com/problems/distinct-subsequences">115. Distinct Subsequences</a></h2><h3>Hard</h3><p>Given two strings s and t, return <i>the number of distinct</i> <b><i>subsequences</i></b><i> of </i>s<i> which equals </i>t.</p>

<p>The test cases are generated so that the answer fits on a 32-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;rabbbit&quot;, t = &quot;rabbit&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from s.
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babgbag&quot;, t = &quot;bag&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong>
As shown below, there are 5 ways you can generate &quot;bag&quot; from s.
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>



### Solving approach:  


![115-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day54/LC115-th.jpg)


 
### My Solution：

  
```python

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            dp[i][0] = 1
        
        for i in range(1,len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * m), where n is the length of s and m is the length of t.
  
- *`Space Complexity`*:<br>
O(n * m), proportional to the size of the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>





