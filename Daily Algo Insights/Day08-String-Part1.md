# Day08 01/02/2024 
## Contents
* [344.Reverse String](#344)
* [541.Reverse StringII](#541)
* [Kama 54](#54)
* [151. Reverse Words in a String](#151)
* [Kama 55](#55)

<h2 id="344"><a href="https://leetcode.com/problems/reverse-string">344. Reverse String</a></h2><h3>Easy</h3><hr><p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>

<p>You must do this by modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> with <code>O(1)</code> extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.</li>
</ul>


### Solving approach:
1. 可以使用two pointers，替换头和尾并依次增加指针。前提是type 要 mutable。
2. 用slicing [::-1] 直接替换
3. 可以用 s.reverse() 直接替换原列表或 text = reverse(s) 生成一个新列表

#### My Solution 1：_`Two Pointers`_
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers
        left, right = 0, len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

```
**Complexity Analysis:**

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(1)

#### My Solution 2：_`Slicing`_
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]

        # reversed V.S reverse
        # s[:] = reversed(s)  with iterable parameter
        # s.reverse() no parameter in ()

        # reverse(0 can only be used with lists and reveses the element of the list in place
        # reversed can work with any iterable(lists, tuples, strings,etc). It doesn't modify the original iterable instead
        # it creates a reverse iterator 

```

**Complexity Analysis:**

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(1)
