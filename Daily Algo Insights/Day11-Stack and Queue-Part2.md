# Day11 - Stack and Queue Part 2

## Contents
* [20. Valid Parentheses](#20)
* [1047. Remove All Adjacent Duplicates In String](#1047)
* [150. Evaluate Reverse Polish Notation](#150)


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
<br>

### Breakdown and Thought Process:  
<br>

**Three invalid cases:**  
<br>
1. First case: The left parenthesis is unnecessary.<br>
![case1](https://github.com/samuelusc/Algomuscle/blob/main/assets/day11-case1.png)

2. Second case: The left bracket doesn't match with the right braces.<br>
![case1](https://github.com/samuelusc/Algomuscle/blob/main/assets/day11-case2.png)

3. Third case: Two unnecessary parentheses on the right.<br>
![case1](https://github.com/samuelusc/Algomuscle/blob/main/assets/day11-case3.png)

**How to fill parentheses into the stack**  

![valid-brackets](https://github.com/samuelusc/Algomuscle/blob/main/assets/day11-valid-brackets.gif)

#### Solving approach 1:

- 考虑使用 `set()`- 每组括号为一个元素 {'()','{}','[]'}， 循环读取s中每一个字符。2种情况 1.遇到左括号，直接加入stack.
  
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
- 当看到将`相邻且相等`的字符删除，考虑用LIFO->Stack。用 for 循环并处理三种情况 1.stack 空则添加元素，
2.stack非空且stack内最后一个元素与读取到char相等，则弹出stack。3. 如果不等，则添加元素.
- 从操作上看有两种情况，1. 弹出stack: stack非空 & stack[-1]==char 2. 添加元素： stack空，or stack[-1] != char 

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

*****

<h2 id='150'><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation">150. Evaluate Reverse Polish Notation</a></h2><h3>Medium</h3><p>You are given an array of strings <code>tokens</code> that represents an arithmetic expression in a <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.</p>

<p>Evaluate the expression. Return <em>an integer that represents the value of the expression</em>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The valid operators are <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, <code>&#39;*&#39;</code>, and <code>&#39;/&#39;</code>.</li>
	<li>Each operand may be an integer or another expression.</li>
	<li>The division between two integers always <strong>truncates toward zero</strong>.</li>
	<li>There will not be any division by zero.</li>
	<li>The input represents a valid arithmetic expression in a reverse polish notation.</li>
	<li>The answer and all the intermediate calculations can be represented in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;2&quot;,&quot;1&quot;,&quot;+&quot;,&quot;3&quot;,&quot;*&quot;]
<strong>Output:</strong> 9
<strong>Explanation:</strong> ((2 + 1) * 3) = 9
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;4&quot;,&quot;13&quot;,&quot;5&quot;,&quot;/&quot;,&quot;+&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (4 + (13 / 5)) = 6
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;10&quot;,&quot;6&quot;,&quot;9&quot;,&quot;3&quot;,&quot;+&quot;,&quot;-11&quot;,&quot;*&quot;,&quot;/&quot;,&quot;*&quot;,&quot;17&quot;,&quot;+&quot;,&quot;5&quot;,&quot;+&quot;]
<strong>Output:</strong> 22
<strong>Explanation:</strong> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tokens.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tokens[i]</code> is either an operator: <code>&quot;+&quot;</code>, <code>&quot;-&quot;</code>, <code>&quot;*&quot;</code>, or <code>&quot;/&quot;</code>, or an integer in the range <code>[-200, 200]</code>.</li>
</ul>


#### Solving approach 1:
- 对于此题考虑用stack存储。 在循环读取token考虑两种情况，case1: if数字，数字包括负数和正数。对于负数比如‘-5’，观察可知len(token) > 1, 对于正数直接用isdigit()判断。然后转成int() 推入stack
- case2: 字符。 这里进入else再对四种符号做处理， 每一种符号用if 去判断‘+’，‘-’，‘*’，‘/’， 然后将到数第二个数字与stack底数字进行符号运，并更新stack[-2]。 除法需要考虑 truncate towards 0,
也就是 用一般/ 再用int()转成趋向于0的整数。
- 最后返回stack[-1](只剩一个数字）

#### My Solution 1：_`if-else + Stack`_
```python

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                stack.append(int(token))
            
            else:
                if token == '+':
                    stack[-2] += stack[-1]
                
                elif token == '-':
                    stack[-2] -= stack[-1] 

                elif token == '*':
                    stack[-2] *= stack[-1]
                # division and ensure integer division for negative one
                else:
                    stack[-2] = int(stack[-2] / stack[-1])
                # remove the last element in stack
                stack.pop()

        return stack[-1]

```

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(n)
#### Solving approach 2:
- 观察后发现，Reverse Polish Notation 会先记录两个数然后是运算符号做计算。考虑使用stack 并对读取的token 做三种判断 a.是否为数字, 如果是数字则存在stack。b.为符号则从stack弹出两个value 进行计算。c.其他用raise 处理 exceptions.
- 用char.isdigit()检查是否数字。这时会遇到一个问题，如何处理负数比如‘-15’？ 由于isdigit() 只能判断positive number,可以考虑定义 is_integer()函数，并单独处理 negative number 情况。
- 判断输入字符是否是“+，-，*，/” 其中之一。 考虑用 Dictionary 这里要 import operator,并将key 设置为这四个符号str，而value则用 operator.add, operator.sub, operator.mul(+-*),
对于/ 需要考虑 1.趋向于0（truncate toward zero) 2. 负数问题。 就这两个问题考虑采用lambda 处理 ：
lambda x,y : int(operator.divtrue(x,y)). divtrue是普通/ 再普通除法。除后再int()取整，python取整是向0取整。
- 最后返回 stack[-1] 


#### My Solution 2：_`Dictionary + Stack`_
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        def is_digit(s):
            if s[0] == '-':
                return s[1:].isdigit()
            return s.isdigit()
        stack = []
        # / 1. operator.truedive(/) 2. floordive (//)
        # 3. lambda x,y: int(operator.truediv(x,y)) truncates toward zero
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda x,y: int(operator.truediv(x, y))}
        for token in tokens:
            if  is_digit(token):
                stack.append(int(token))
            
            elif token in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                # operators['+'](10, 5)  # 等于 10 + 5
                stack.append(operators[token](num2,num1))
            else:
                raise ValueError('Invalid token')

        return stack[-1]

```

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(n)

#### Solving approach 3:
结合答案1与答案2，优化dictionary。 参考 solution 2 中的除法，全部value 用 lambda 替换，这样无需import operator. 比如 '+': lambda x,y : x+y 。只判断2种可能，符号或数字即可

#### My Solution 3：_`Dictionary + lambda`_
```python
#consider both solution 1 and 2 to update solution3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # refer to solution2 lambda x,y: int(x/y) to update dictionary 
        operators = {'+': lambda x,y : x + y,'-': lambda x,y : x - y ,'*': lambda x,y : x * y, '/': lambda x,y : int(x/y) }
        for token in tokens:
            if token in operators:
                stack[-2] = operators[token](stack[-2],stack[-1])
                stack.pop()
            else:
                stack.append(int(token))
        
        return stack[-1]

```

- *`Time Complexity`*:
O(n)
- *`Space Complexity`*:
O(n)
