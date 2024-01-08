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

##### 维护一个queue 保持两个特性: 
1. 保持队列头部的元素最大，如果新加入的比队列中的元素大，则把前面的踢出（新加入的前面一定比他大）。

2. 移动滑窗, 当移动的索引大于window size, 踢出 queue 头部元素。
	
### Solving approach 1:

1. 用双端队列deque, 注意在维护性质1时（元素前边都比它大），用 `while` 而不是 *"if"* 。 

2. 队列列维护的是`index` 而不是 _“number”_

3. 当队列首位所对应的index 超出window size, 则踢出，当在window size 范围内则加入最终结果

### My Solution 1：_`Monotonic deque`_  

  
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
O(n) where n is the number of elements in the array since each element is only pushed into and poped out of deque once.
  
- *`Space Complexity`*:
O(n) as there may be at most n elements in the deque.
---

![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/dividingline.gif)

### Breakdown and Thought Process:  
<br>

1. 维护一个最大`k 频率`的列表，首先想到可以用模块collections下的Counter 子类，去获取每个数字对应的频率。 如果对它进行排序并抽取最大的k个那么就可以得到结果，时间复杂度O(nlogn)

2. `Follow up`: 如果要降低复杂度就需要降低`logn`，我们不需要*n个*最大频率 而只需要`k个`。考虑最大字样则联想到Heap, Max Heap 和 Min Heap 我们选择 Min Heap 因为需要维护size K,而 min heap 可以轻易弹出最小元素。

### Solving approach: O(nlogk)

1. Solution1 是优化过的，我们使用了 `Min-heap`。这里注意两件事 1. Count类似于字典，其key是num 而value则是频率 : for key,value in counts.items()。 

用python 的heapq 记得带上num: heappush(min_heap(freq, num), 因为最后我们需要返回num 另外当frequency 相同时，将会以num 作为min heap排序标准

2. len(min_heap) > k 则踢出最小的tuple(freq,num), 留下的就是我们需要的。最后循环处理min_que,留下tuple中的第二个元素。

### My Solution 1：_`heapq(min heap)`_  

  
```python

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import heappush, heappop
        min_heap =[]
        
        # count frequency of each number in nums by Counter
        counts = Counter(nums)

        #Iterate through counts for each pair(number, frequency)
        for num, freq in counts.items():
            # push a pair of tuple into heap
            heappush(min_heap, (freq, num))
            # check if the heap size exceed k
            if len(min_heap) > k:
                heappop(min_heap)
        
        #extract the top k frequency number(index 2) from tuple 
        top_k = [pair[1] for pair in min_heap]

	# don't forget return the list top_k
        return top_k
        

```

- *`Time Complexity`*:
O(nlogk), where there are n heap push and pop operations, each taiking O(log k) time. 
  
- *`Space Complexity`*:
O(n+k)-> O(n) , n is the size of counter and k is the size of heap. since k is less than n, therefore the space can be O(n)
---
  
### Solving approach 2:  O(nlogn)

1. *未经过优化* 这里用了 collections.Counter()下面的一个方法: `most_common(k)`, 可以获取计数器中频率最高的k个元素和他们的频率。

2. 用 ele for ele, fre in counts.most_common(k), 进行循环解包并返回element。最后生成 top_k 列表
 
### My Solution 2：_`most_common(k)`_  

  
```python

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Use Counter to count the occurrence of each number in nums
        counts = Counter(nums)
        # Retrieve the top k most frequent elements
        # most_common() returns a list of tuples, unpacking them here
        top_k = [element for element, count in counts.most_common(k)]

        return top_k

```

**Complexity Analysis:**  

- *`Time Complexity`*:
O(nlogn)
  
- *`Space Complexity`*:
O(n)
---

![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/dividingline.gif)










