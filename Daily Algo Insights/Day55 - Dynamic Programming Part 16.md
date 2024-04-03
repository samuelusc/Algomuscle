# Day55 - Dynamic Programming Part 16


## Contents
* **[583. Delete Operation for Two Strings](#583)**
* **[72. Edit Distance](#72)**


<br>
<h2 id = "583"><a href="https://leetcode.com/problems/delete-operation-for-two-strings">583. Delete Operation for Two Strings</a></h2><h3>Medium</h3><hr><p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of <strong>steps</strong> required to make</em> <code>word1</code> <em>and</em> <code>word2</code> <em>the same</em>.</p>

<p>In one <strong>step</strong>, you can delete exactly one character in either string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;sea&quot;, word2 = &quot;eat&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need one step to make &quot;sea&quot; to &quot;ea&quot; and another step to make &quot;eat&quot; to &quot;ea&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;leetcode&quot;, word2 = &quot;etco&quot;
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of only lowercase English letters.</li>
</ul>


### Solving approach 1:


[53-thought-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day55/LC583-th_1.jpg)
[53-thought-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day55/LC583-th_2.jpg)



### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1)+1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        for i in range(1,len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)
        
        return dp[-1][-1]
```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * m). Thus, the time complexity is O(n * m), where n is the length of word1 and m is the length of word2.
  
- *`Space Complexity`*:<br>
O(n * m), proportional to the dimensions of the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "72"><a href="https://leetcode.com/problems/edit-distance">72. Edit Distance</a></h2><h3>Medium</h3><hr><p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>




### Solving approach:  


[72-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day55/LC72-th.jpg)


 
### My Solution：

  
```python

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i
        
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)

        return dp[-1][-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n * m), where n is the length of word1 and m is the length of word2.


  
- *`Space Complexity`*:<br>
O(n * m), proportional to the size of the dp array.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>





