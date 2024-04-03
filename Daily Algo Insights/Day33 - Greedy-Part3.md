# Day33 - Greedy Part3


## Contents
* **[1005. Maximize Sum Of Array After K Negations](#105)**
* **[134. Gas Station](#134)**
* **[135. Candy](#135)**

<br>

<h2 id = "1005"><a href="https://leetcode.com/problems/maximize-sum-of-array-after-k-negations">1005. Maximize Sum Of Array After K Negations</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, modify the array in the following way:</p>

<ul>
	<li>choose an index <code>i</code> and replace <code>nums[i]</code> with <code>-nums[i]</code>.</li>
</ul>

<p>You should apply this process exactly <code>k</code> times. You may choose the same index <code>i</code> multiple times.</p>

<p>Return <em>the largest possible sum of the array after modifying it in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> Choose index 1 and nums becomes [4,-2,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,-1,0,2], k = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,-3,-1,5,-4], k = 2
<strong>Output:</strong> 13
<strong>Explanation:</strong> Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>
### Breakdown and Thought Process:  
<br>


### My Solution 1：_`two time-Greedy`_  

  
```python

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #两次贪心 1.negative number 2. smallest number

        nums.sort(key = lambda x : -abs(x))

        for i in range(len(nums)):
            if k > 0 and nums[i]< 0:
                nums[i] *= -1
                k -= 1

        # 通过判断k的奇偶数，是否改变nums[-1]
        if k % 2 != 0:
            nums[-1] *= -1
        
        return sum(nums)    

```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(nlogn), where n is the number of elements in nums. 
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "134"><a href="https://leetcode.com/problems/gas-station">134. Gas Station</a></h2><h3>Medium</h3><hr><p>There are <code>n</code> gas stations along a circular route, where the amount of gas at the <code>i<sup>th</sup></code> station is <code>gas[i]</code>.</p>

<p>You have a car with an unlimited gas tank and it costs <code>cost[i]</code> of gas to travel from the <code>i<sup>th</sup></code> station to its next <code>(i + 1)<sup>th</sup></code> station. You begin the journey with an empty tank at one of the gas stations.</p>

<p>Given two integer arrays <code>gas</code> and <code>cost</code>, return <em>the starting gas station&#39;s index if you can travel around the circuit once in the clockwise direction, otherwise return</em> <code>-1</code>. If there exists a solution, it is <strong>guaranteed</strong> to be <strong>unique</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> gas = [1,2,3,4,5], cost = [3,4,5,1,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> gas = [2,3,4], cost = [3,4,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
You can&#39;t start at station 0 or 1, as there is not enough gas to travel to the next station.
Let&#39;s start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can&#39;t travel around the circuit once no matter where you start.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == gas.length == cost.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= gas[i], cost[i] &lt;= 10<sup>4</sup></code></li>
</ul>
### Breakdown and Thought Process:  
<br>


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, cur_sum, start = 0, 0, 0

        for i in range(len(cost)):
            cur_sum += gas[i] - cost[i]
            total += gas[i] -cost[i]

            if cur_sum < 0:
                cur_sum = 0
                start = i + 1

        return start if total >= 0 else -1
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n),  where n is the number of gas stations.
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



<h2><a href="https://leetcode.com/problems/candy">135. Candy</a></h2><h3>Hard</h3><hr><p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have at least one candy.</li>
	<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>Return <em>the minimum number of candies you need to have to distribute the candies to the children</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>



### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def candy(self, ratings: List[int]) -> int:
        

        allocate = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                # 注意这里应该是 allocate[i-1] + 1 而不是 allocate[i] + 1
                allocate[i] = allocate[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                allocate[i] = max(allocate[i], allocate[i+1] + 1) 

        return sum(allocate)   
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of children (or the length of the ratings list).
  
- *`Space Complexity`*:<br>
O(n)
