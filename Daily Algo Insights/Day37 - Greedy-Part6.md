# Dayxx - xxxxxx

### [Study Reference](https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html)  

## Contents
* **[738. Monotone Increasing Digits](#738)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**

<br>
<h2><a href="https://leetcode.com/problems/monotone-increasing-digits">738. Monotone Increasing Digits</a></h2><h3>Medium</h3><hr><p>An integer has <strong>monotone increasing digits</strong> if and only if each pair of adjacent digits <code>x</code> and <code>y</code> satisfy <code>x &lt;= y</code>.</p>

<p>Given an integer <code>n</code>, return <em>the largest number that is less than or equal to </em><code>n</code><em> with <strong>monotone increasing digits</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1234
<strong>Output:</strong> 1234
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 332
<strong>Output:</strong> 299
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![Thought process - Q738](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day37/Leetcode56-thought.jpg)



### My Solution 1：

  
```python

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        n_list = list(str(n))
        
        # 从后向前list(size, x + 1 = 实际停止位置， -1)
        for i in range(len(n_list)-1,0,-1):
            if n_list[i-1] > n_list[i]:
                n_list[i-1] = str(int(n_list[i-1]) - 1)
                n_list[i:] = "9" * (len(n_list) - i)

        #最后除了拼接成string 还需要转成 integer
        return int("".join(n_list))
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx




### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx



### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx



