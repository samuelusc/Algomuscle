# Day37 - Greedy Part5


## Contents
* **[435. Non-overlapping Intervals](#435)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
<br>
xxximagexxx
<br>
<h2><a href="https://leetcode.com/problems/non-overlapping-intervals">435. Non-overlapping Intervals</a></h2><h3>Medium</h3><hr><p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code></li>
</ul>


<br>

### Solving approach 1:

[452 Similar Question/Day 35](https://github.com/samuelusc/Algomuscle/blob/main/Daily%20Algo%20Insights/Day35%20-%20Greedy-Part4.md#452)

![Thought-process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day36/Leetcode435-thoutht.jpg)


 
### My Solution 1：_`sort + greedy`_  

  
```python

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],x[1]))
        count = 0

        # 设定第一个比较对象
        pre_end = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < pre_end:
                count += 1
                pre_end = min(pre_end, intervals[i][1])
            # 更新 pre_end
            else:
                pre_end = intervals[i][1]

        
        return count
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(nlogn), where n is the length of the interval list.
  
- *`Space Complexity`*:<br>
O(1)  
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




xxxxx



### My Solution 1：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



xxxx


### My Solution 1：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx







