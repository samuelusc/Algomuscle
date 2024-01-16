# Day07 - HashMap Part 2


## Contents
* **[454.4Sum II](#454)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**

<br>
<h2 id = "454"><a href="https://leetcode.com/problems/4sum-ii">454. 4Sum II</a></h2><h3>Medium</h3><hr><p>Given four integer arrays <code>nums1</code>, <code>nums2</code>, <code>nums3</code>, and <code>nums4</code> all of length <code>n</code>, return the number of tuples <code>(i, j, k, l)</code> such that:</p>

<ul>
	<li><code>0 &lt;= i, j, k, l &lt; n</code></li>
	<li><code>nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The two tuples are:
1. (0, 0, 0, 1) -&gt; nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt; nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>n == nums3.length</code></li>
	<li><code>n == nums4.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>-2<sup>28</sup> &lt;= nums1[i], nums2[i], nums3[i], nums4[i] &lt;= 2<sup>28</sup></code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


- 选择 `dicitionary` 记录 `a+b 的个数`， 然后迭代查找 `c+d 的补数`在 dictionary 中的累计个数。


### My Solution 1：_`Dictionary + complement`_  

  
```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 用dictionary, {key: a+b value: count}
        hashmap = {}

        for a in nums1:
            for b in nums2:
                #如果a+b已经在hashmap中则返回count+1，否则返回 0 + 1
                hashmap[a+b] = hashmap.get(a+b, 0) + 1

        #initialize complement number of c+d
        count = 0
        
        for c in nums3:
            for d in nums4:
                target= -(c+d)
                # not hashmap.get(target, 0) + 1
                # 累计球 c+d 补数的数量
                # 如果有多个c+d 则会每个这样的组合都会被考虑在内
                count += hashmap.get(target, 0)

        return count

```

### My Solution 2：_`Counter + complement`_  

  
```python

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 使用Counter计算 {Key: a+b Value: count}
        from collections import Counter
        
        # list comprehension 计算a+b 的数量并生成一个dictionary
        ab_sum = Counter(a+b for a in nums1 for b in nums2)
        
        return sum(ab_sum[-(c+d)]for c in nums3 for d in nums4)
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2) where n is the number of operations performed.
  
- *`Space Complexity`*:<br>
O(n^2). The Counter holds at most n^2 entries, corresponding to each unique sum of elements from nums1 and nums2.


<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



xxxx








