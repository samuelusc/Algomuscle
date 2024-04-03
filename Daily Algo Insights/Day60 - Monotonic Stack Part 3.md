# Day60 - Monotonic Stack Part 3


## Contents
* **[84. Largest Rectangle in Histogram](#84)**


<br>
<h2 id = "84"><a href="https://leetcode.com/problems/largest-rectangle-in-histogram">84. Largest Rectangle in Histogram</a></h2><h3>Hard</h3><p>Given an array of integers <code>heights</code> representing the histogram&#39;s bar height where the width of each bar is <code>1</code>, return <em>the area of the largest rectangle in the histogram</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" style="width: 522px; height: 242px;" />
<pre>
<strong>Input:</strong> heights = [2,1,5,6,2,3]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" style="width: 202px; height: 362px;" />
<pre>
<strong>Input:</strong> heights = [2,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>


 
### My Solution：

  
```python

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        leverage monotonically decreasing stack to solve the question
        """
        #make the monotonic structure worked
        heights = [0] + heights + [0]
        stack = [0]
        res = 0
        #construct the decreasing stack 
        for i in range(1,len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)

            else:
                while stack and heights[i]<heights[stack[-1]]:
                    mid = stack.pop()

                    if stack:
                        left = stack[-1]
                        right = i

                        w = right - left -1
                        h = heights[mid]

                        res = max(h*w, res)
                
                stack.append(i)
        
        return res


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of elements in the original heights array.
  
- *`Space Complexity`*:<br>
O(n), where n is the length of the original heights array.

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>











