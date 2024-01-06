# Day11 - Stack and Queue Part 2

## Contents
* [20. Valid Parentheses](#20)
* [1047. Remove All Adjacent Duplicates In String](#1047)
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

<h2 id = "1047"><a href="https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string">1047. Remove All Adjacent Duplicates In String</a></h2><h3>Easy</h3><p>You are given a string <code>s</code> consisting of lowercase English letters. A <strong>duplicate removal</strong> consists of choosing two <strong>adjacent</strong> and <strong>equal</strong> letters and removing them.</p>

<p>We repeatedly make <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It can be proven that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbaca&quot;
<strong>Output:</strong> &quot;ca&quot;
<strong>Explanation:</strong> 
For example, in &quot;abbaca&quot; we could remove &quot;bb&quot; since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is &quot;aaca&quot;, of which only &quot;aa&quot; is possible, so the final string is &quot;ca&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;azxxzy&quot;
<strong>Output:</strong> &quot;ay&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

#### Solving approach 1:
- 当看到`相邻且相等字符`删除，考虑用LIFO->Stack。用 for 循环并处理三种情况 1.stack 空则添加元素，
2.stack非空且stack内最后一个元素与读取到char相等，则弹出stack。3. 如果不等，则添加元素.
- 从操作上看有两种情况，1. 弹出stack: stack非空 & stack[-1]==char 2. 添加元素： stack空，stack[-1] != char 

#### My Solution 1：_`stack`_
```python
class Solution:
    def removeDuplicates(self, s: str) -> str:

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            
            else:
                stack.append(char)

        
        return ''.join(stack)

            
            

```

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(n)
#### Solving approach:
- 
#### My Solution 2：_`xxx`_
```python


```

**Complexity Analysis:**

- *`Time Complexity`*:

- *`Space Complexity`*:




