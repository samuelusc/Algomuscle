# Day36 - Greedy Part5


## Contents
* **[435. Non-overlapping Intervals](#435)**
* **[763. Partition Labels](#763)**
* **[56. Merge Intervals](#56)**


<br>
<h2 id = "435"><a href="https://leetcode.com/problems/non-overlapping-intervals">435. Non-overlapping Intervals</a></h2><h3>Medium</h3><p>Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.</p>

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

- [452 Similar Question - 452. Minimum Number of Arrows to Burst Balloons](https://github.com/samuelusc/Algomuscle/blob/main/Daily%20Algo%20Insights/Day35%20-%20Greedy-Part4.md#452)

![Thought-process-435](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day36/Leetcode435-thoutht.jpg)


 
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




<h2 id = "763"><a href="https://leetcode.com/problems/partition-labels">763. Partition Labels</a></h2><h3>Medium</h3><p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in at most one part.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resultant string should be <code>s</code>.</p>

<p>Return <em>a list of integers representing the size of these parts</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababcbacadefegdehijhklij&quot;
<strong>Output:</strong> [9,7,8]
<strong>Explanation:</strong>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits s into less parts.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;eccbbbbdec&quot;
<strong>Output:</strong> [10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>



### Solving approach 1:


![Thought-process-763](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day36/Leetcode763-thoght%20.jpg)




### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = [0] * 26
        res = []
        for i in range(len(s)):
            hashmap[ord(s[i]) - ord('a')] = i
        print(hashmap)


        left, right = 0, 0
        for i in range(len(s)):
            right = max(right, hashmap[ord(s[i])-ord("a")])

            if right == i:
                #return the size of the part +1
                res.append(right - left + 1)
                left = i+1


        return res
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



<h2 id = "56"><a href="https://leetcode.com/problems/merge-intervals">56. Merge Intervals</a></h2><h3>Medium</h3><p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


### Solving approach 1:

- [Similar Question - 452. Minimum Number of Arrows to Burst Balloons](https://github.com/samuelusc/Algomuscle/blob/main/Daily%20Algo%20Insights/Day35%20-%20Greedy-Part4.md#452)
- [Similar Question - 435. Non-overlapping Intervals](#435)

![Thought-process-56](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day36/Leetcode56-thought1.jpg)



### My Solution 1：_`greedy left`_  

  
```python

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: (x[0],x[1]))

        # contrain 已经表明 intervals.size >= 1
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])

            else:
                res.append(intervals[i])

        return res



        
       
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(nlogn)
  
- *`Space Complexity`*:<br>
O(1) if we don't consider output space which can be O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>
