# Day13 - Stack and Queue Part 3

## Contents
* **[239. Sliding Window Maximu](239)**
* **[347. Top K Frequent Elements](347)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
<br>

![Day13](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day13/Day13.png)

<br>
<h3 id ='239'><a href="https://leetcode.com/problems/sliding-window-maximum">239. Sliding Window Maximum</a></h2><h3>Hard</h3><p>You are given an array of integers&nbsp;<code>nums</code>, there is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the max sliding window</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong> 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>

### Breakdown and Thought Process:  
<br>

`Input`: [1,3,2,5,8,7]  k = 3  
  
`Output`: 1 [3,5,8,8] <br>

![Day13](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day13/day13-239presentation.png)

**Animated demonstration** <br>
![Day13](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day13/day12-239process.gif) <br>

##### 维护一个对列保持两个特性: 1. 保持队列头部的元素最大，如果新加入的比队列中的元素大，则把前面的踢出（新加入的前面一定比他大）。 2. 移动滑窗, 当移动的索引大于window size, 踢出 queue 头部元素。
	
#### Solving approach 1:
<br>


#### My Solution 1：_`xxx`_  

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:       
        # initialize deque
        queue = deque()
        res = []
        #acquire each index and value by iterating through nums
        for i, num in enumerate(nums):
            
            # Notice not "if" here, 
            # we iterately remove every numbers in the queue,
            # that is less than the current one before it 
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            # Notice! push current index into queue
            queue.append(i)
            #remove the first ele if it's outside the window
            if queue[0] == i - k:
                queue.popleft()
            # check if the length at the current position has
            # reached the required window size
            if i + 1 >= k:
                res.append(nums[queue[0]])

        return res

                
```

- *`Time Complexity`*:

  
- *`Space Complexity`*:
---

![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/dividingline.gif)











