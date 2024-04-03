# Day57 -  Dynamic Programming Part 17


## Contents
* **[647. Palindromic Substrings](#647)**
* **[516. Longest Palindromic Subsequence](#516)**


<br>
<h2 id = "647"><a href="https://leetcode.com/problems/palindromic-substrings">647. Palindromic Substrings</a></h2><h3>Medium</h3><p>Given a string <code>s</code>, return <em>the number of <strong>palindromic substrings</strong> in it</em>.</p>

<p>A string is a <strong>palindrome</strong> when it reads the same backward as forward.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three palindromic strings: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaa&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> Six palindromic strings: &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;aa&quot;, &quot;aa&quot;, &quot;aaa&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![647-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day57/LC647-th_1.jpg)
![647-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day57/LC647-th_2.jpg)



### My Solution：

  
```python

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]

        res = 0
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2: 
                        dp[i][j] = True
                        res += 1
                    elif dp[i+1][j-1] == True:
                        dp[i][j] = True
                        res += 1

        return res               
                        
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n²), where n is the length of s.
  
- *`Space Complexity`*:<br>
O(n²), due to the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




<h2 id = "516"><a href="https://leetcode.com/problems/longest-palindromic-subsequence">516. Longest Palindromic Subsequence</a></h2><h3>Medium</h3><p>Given a string <code>s</code>, find <em>the longest palindromic <strong>subsequence</strong>&#39;s length in</em> <code>s</code>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbab&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible longest palindromic subsequence is &quot;bbbb&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> One possible longest palindromic subsequence is &quot;bb&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>



### Solving approach:  


![516](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day57/LC516-th.jpg)

 
### My Solution：

  
```python

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1


        for i in range(len(s)-1, -1,-1):
            for j in range(i+1, len(s)):

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2

                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) 

        return dp[0][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n²), where n is the length of s.
  
- *`Space Complexity`*:<br>
O(n²), due to the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


