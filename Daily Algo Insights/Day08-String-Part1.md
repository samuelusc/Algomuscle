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

<h2 id="541"><a href="https://leetcode.com/problems/reverse-string-ii">541. Reverse String II</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> and an integer <code>k</code>, reverse the first <code>k</code> characters for every <code>2k</code> characters counting from the start of the string.</p>

<p>If there are fewer than <code>k</code> characters left, reverse all of them. If there are less than <code>2k</code> but greater than or equal to <code>k</code> characters, then reverse the first <code>k</code> characters and leave the other as original.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcdefg", k = 2
<strong>Output:</strong> "bacdfeg"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "bacd"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

### Solving approach:
1. right: left + k ， 用于反转。 left: left + 2*k 作为步长。 再用left < s 长度
2. 最开始写时，没有意识到slicing的索引可以超过他的长度。所以用两个if 处理边界问题， 再用for loop 去循环处理2k以上长度的s。
3. 直接用一个for loop 设定步长2*k, 每一次反转i+k ->使用 reversed[i:i+k]
 

#### My Solution 1：_`Two Pointers + Slicing`_
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Initialize a left pointer to track the start of each 2k segment.
        left = 0


        while left < len(s):

            # Calculate the right boundary for the k characters to be reversed.
            right = left + k
            
            # Reverse the k characters starting from 'left' and ending at 'right'.
            # Concatenate it with the non-reversed parts of the string.
            s = s[:left] + s[left:right][::-1] + s[right:]

            # Move the left pointer forward by 2k to process the next segment.
            left = left + 2 * k
        
        # Return the modified string after processing all segments.
        return s

# T: O(n^2/k) S: O(n)

# each iteration process 2k and run n/2k. at each iteration to process slicing and string will be O(n). In total it's about O(n^2/k)

```

- *`Time Complexity`*:
O(n^2/k) Each iteration process 2k and run n/2k. at each iteration to process slicing and string will be O(n). In total it's about O(n^2/k)

- *`Space Complexity`*:
O(n)

#### My Solution 2：_`xxx`_
```python
# T: O(n), S: O(n)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            # create new string and assign to s
            return s[::-1]
        
        elif len(s) < 2*k:
            return s[:k][::-1] + s[k:]

        # convert string to list  
        s = list(s)
        for i in range(0,len(s), 2*k):
                            
            # If the remaining characters are less than k, reverse them and return the string
            if len(s) - i < k:
                
                # Use join() to convert the list back to a string
                return "".join(s[:i] + s[i:][::-1])
            # Reverse the next k characters in place
            s[i:i+k] = s[i:i+k][::-1]
        
        return "".join(s)
# In Python, when you slice a string with an index that is beyond the string's actual length, 
# Python will not throw an error. Instead, it will adapt to the situation and return as many characters as possible.
```

**Complexity Analysis:**

- *`Time Complexity`*:

- *`Space Complexity`*:

#### My Solution 3：_`xxx`_
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        text = list(s)

        for i in range(0, len(text), 2*k):

            #reverse first k 
            #eventhough the lenght of remaining elements is less than k 
            text[i:i+k] = reversed(text[i: i+k])
        
        return "".join(text)

#T: O(n), S: O(n)

```

**Complexity Analysis:**

- *`Time Complexity`*:
O(n)

- *`Space Complexity`*:
O(n)

## 54 替换数字<a name="54"></a>
<a href="https://programmercarl.com/kama54.%E6%9B%BF%E6%8D%A2%E6%95%B0%E5%AD%97.html#%E6%80%9D%E8%B7%AF" target="_blank">54.替换数字</a>

给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。
#### 输入描述
输入一个字符串 s,s 仅包含小写字母和数字字符。
#### 输出描述
打印一个新的字符串，其中每个数字字符都被替换为了number
#### 输入示例
a1b2c3
#### 输出示例
anumberbnumbercnumber
#### 提示信息
**数据范围：**
`1 <= s.length < 10000。`

### Solving approach:
循环读取每一个letter, 用 char.isdigit() 确认是否数字，如果True 就 text + “number”, 否则 text + char

#### My Solution 1：_`xxx`_
```python
class Solution:
    def convertNumber(self, s: str)->str:
        
        text =''
        
        for char in s:
            if char.isdigit():
                text += "number"
            
            else:
                text += char
        
        return text
            
        
sol = Solution()
s = input()

res = sol.convertNumber(s)
print(res)

```

**Complexity Analysis:**

- *`Time Complexity`*:
O(n)

- *`Space Complexity`*:
O(n)

<h2 id="151"><a href="https://leetcode.com/problems/reverse-words-in-a-string">151. Reverse Words in a String</a></h2><h3>Medium</h3><hr><p>Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.</p>

<p>A <strong>word</strong> is defined as a sequence of non-space characters. The <strong>words</strong> in <code>s</code> will be separated by at least one space.</p>

<p>Return <em>a string of the words in reverse order concatenated by a single space.</em></p>

<p><b>Note</b> that <code>s</code> may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;the sky is blue&quot;
<strong>Output:</strong> &quot;blue is sky the&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;  hello world  &quot;
<strong>Output:</strong> &quot;world hello&quot;
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a good   example&quot;
<strong>Output:</strong> &quot;example good a&quot;
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>&#39; &#39;</code>.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
</ul>

<p>&nbsp;</p>
<p><b data-stringify-type="bold">Follow-up:&nbsp;</b>If the string data type is mutable in your language, can&nbsp;you solve it&nbsp;<b data-stringify-type="bold">in-place</b>&nbsp;with&nbsp;<code data-stringify-type="code">O(1)</code>&nbsp;extra space?</p>

### Solving approach:


#### My Solution 1：_`xxx`_
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        #s.strip() remove start and end space
        # split() will remove space in s including start and end
        words = s.split()
        # reverse in place
        words.reverse()
        return ' '.join(words)

```

- *`Time Complexity`*:
O(n) where n is the length of "s"
- *`Space Complexity`*:
O(n) where n is the length of "s"
#### My Solution 2：_`xxx`_
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()

        left, right = 0, len(text)-1
        while left < right:
            text[left],text[right] = text[right],text[left]
            left += 1
            right -= 1
        
        return " ".join(text)

# T：O(n) where n is the length of "s"
# S: O(n) where n is the length of "s"

```

**Complexity Analysis:**

- *`Time Complexity`*:
O(n) where n is the length of "s"
- *`Space Complexity`*:
O(n) where n is the length of "s"
