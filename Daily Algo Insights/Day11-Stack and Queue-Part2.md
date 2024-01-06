# Day11 - Stack and Queue Part 2

## Contents
* [20.Valid Parentheses](#20)
* [xx](#)
* [xx](#)
* [xx](#)
* [xx](#)

<h2 id = "20"><a href="https://leetcode.com/problems/valid-parentheses">20. Valid Parentheses</a></h2><h3>Easy</h3><p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>



#### Solving approach 1:
- 考虑使用 `set()`- 每组括号为一个元素 {'()','{}','[]'}， 循环读取s中每一个字符。2种情况 1.遇到左括号，直接加入stack 
2.遇到右括号 a.stack为空则直接返回False b.stack弹出字符和读取的字符无法匹配set,返回 False。 
- 最后查看stack，空返回 True 否则 False

#### My Solution 1：_`set()`_
```python
class Solution:
    def isValid(self, s: str) -> bool:
        # 设置每对字符串作为set元素
        hashset = {'()','{}','[]'}
        stack = []

        #遇到左括号的情况
        #遇到右括号的情况（stack中无左括号，stack中左括号和右括号不相匹配）
        for char in s:
            # 把这三类左括号当成迭代对象去确认，中间无逗号。放入stack            
            if char in '({[':
                stack.append(char)
            # 1 stack 为空 2. 左右不匹配 则返回 False
            elif not stack or stack.pop() + char not in hashset:
                return False
        
        # 如果stack 空，则返回True
        return not stack

```

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(n)
#### Solving approach 2:
- 考虑使用dictionary: {'(': ')', '{':'}', '[':']'},关键在于将左括号作为key,右括号作为value。 如果stack空或者与弹出的item.value不匹配则返回False。
- 如果stack为空返回True
#### My Solution 2：_`dict()`_
```python
class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid(self, s: str) -> bool:
        # write your code here
        stack =[]
        hashmap = {'(':')', '[':']','{':'}'}
        for char in s:
            if char in '([{':
                stack.append(char)
            
            elif not stack or hashmap[stack.pop()] != char:
                return False
        
        return not stack

```

**Complexity Analysis:**

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(n)

*****








