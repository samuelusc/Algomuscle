# Day09 - String Part 2

## Contents
* [28. Find the Index of the First Occurrence in a String](#28)
* [459. Repeated Substring Pattern](#459)
* [xx](#)
* [xx](#)
* [xx](#)


<h2 id="28"><a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string">28. Find the Index of the First Occurrence in a String</a></h2><h3>Easy</h3><hr><p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;sad&quot; occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>

### Solving approach:


#### My Solution 1：_`for + slicing`_
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Slicing approach

        h_len, n_len = len(haystack), len(needle)

        if h_len < n_len:
            return -1
        
        for i in range(0, h_len - n_len + 1):
            if haystack[i: i + n_len] == needle:
                return i
        
        return -1

	# return haystack.find(needle) 
	# if find needle ,will return start index in haystack or return  - 1 if can't it.
	# string.find(substring, start, end) optional: (start, end)
```

- *`Time Complexity`*:
O((n-m+1) * m) -> O(n*m)
- *`Space Complexity`*:
O(1)
### Solving approach:

#### My Solution 2：_`two pointers(for+while)`_
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len,n_len = len(haystack), len(needle)
        
        # boundary check
        if h_len < n_len:
            return -1
        # iterate through haystack 
        for i in range(0,h_len - n_len + 1):
            
            left,right = i, 0

            # if the letter of haystack is the same as needle
            if haystack[left] == needle[right]:
                while right < n_len:
                                       
                    if haystack[left] != needle[right]:
                        break
                    if right == n_len-1:
                        return i

                    left += 1
                    right += 1
        return -1

```

**Complexity Analysis:**

- *`Time Complexity`*:
O((n-m+1) * m) -> O(n*m)
- *`Space Complexity`*:
O(1)

<h2 id ="459"><a href="https://leetcode.com/problems/repeated-substring-pattern">459. Repeated Substring Pattern</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;ab&quot; twice.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcabcabc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;abc&quot; four times or the substring &quot;abcabc&quot; twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

### Solving approach:
可以利用`字符串的重复性质`来检测是否's'可以由它的子字符重复多次构成。如果's'确实可以由其字符串重复构成，那么在2s中找到完全匹配s的初始位置将在第一个s结束前也就是index<len(s).

#### My Solution 1：_`2S`_
```python

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         # create 2s
         double_s = s + s
         index_s = double_s.index(s, 1)

         return index_s < len(s)
         

```

- *`Time Complexity`*:
O(n^2)
- *`Space Complexity`*:
O(n)
### Solving approach:

#### My Solution 2：_`xxx`_
```python


```

**Complexity Analysis:**

- *`Time Complexity`*:

- *`Space Complexity`*:
