# Day42 - Dynamic Programming Part 4


## Contents
* **[46. 携带研究材料-2D/1D](#46)**
* **[416. Partition Equal Subset Sum](#416)**

<br>

### 0-1 Knapsack

![0-1 knapsack-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day42/0-1%20knapsack-%E4%BA%8C%E7%BB%B4_1.jpg)
![0-1 knapsack-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day42/0-1%20knapsack-%E4%BA%8C%E7%BB%B4_2.jpg)
<br>

### 46. 携带研究材料 <a name = "46"></a>
#### [Question Reference](https://kamacoder.com/problempage.php?pid=1046)


小明是一位科学家，他需要参加一场重要的国际科学大会，以展示自己的最新研究成果。他需要带一些研究材料，但是他的行李箱空间有限。这些研究材料包括实验设备、文献资料和实验样本等等，它们各自占据不同的空间，并且具有不同的价值。 

小明的行李空间为 N，问小明应该如何抉择，才能携带最大价值的研究材料，每种研究材料只能选择一次，并且只有选与不选两种选择，不能进行切割。

### 输入描述
第一行包含两个正整数，第一个整数 M 代表研究材料的种类，第二个正整数 N，代表小明的行李空间。

第二行包含 M 个正整数，代表每种研究材料的所占空间。 

第三行包含 M 个正整数，代表每种研究材料的价值。

### 输出描述
输出一个整数，代表小明能够携带的研究材料的最大价值。

#### 输入示例
6 1

2 2 3 1 5 2

2 3 1 5 4 3
#### 输出示例
5

#### 提示信息

小明能够携带 6 种研究材料，但是行李空间只有 1，而占用空间为 1 的研究材料价值为 5，所以最终答案输出 5。 

#### 数据范围：
1 <= N <= 5000

1 <= M <= 5000

研究材料占用空间和价值都小于等于 1000


<br>

### My Solution 1：_`2D`_  

```python

class Solution:
    def knapsack(self, mat_size, capacity, weights, vals):
        
        if capacity < min(weights):
            return 0
            
        dp = [[0] * (capacity+1) for _ in range(mat_size)]
        
        
        for j in range(weights[0], capacity + 1):
            dp[0][j] = vals[0]
    
        
        for i in range(1,mat_size):
            for j in range(capacity + 1):
                if j < weights[i]:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    dp [i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + vals[i])
                    
        
        return dp[-1][-1]
        
        
        
        
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
        
    mat_size = arr[0]
    capacity = arr[1]
        
    weights = [int(x) for x in input().split()]
    vals =[int(x) for x in input().split()]
        
    sol = Solution()
    res = sol.knapsack(mat_size, capacity,weights,vals)
        
    print(res) 
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n^2)
<br>


## Knapsack - 1D:

![0-1 knapsack-1D](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day42/%E8%83%8C%E5%8C%851D.jpg)



### My Solution：_`1D`_  

  
```python

class Solution:
    def knapsack(self, mat_size, capacity, weights, vals):
        
        if capacity < min(weights):
            return 0
            
        dp = [0] * (capacity + 1)
    
        
        for item,val in zip(weights,vals):
            for j in range(capacity, item -1, -1):
                dp[j] = max(dp[j],dp[j-item] + val)

                
    
        return dp[-1]
        
        
        
        
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
        
    mat_size = arr[0]
    capacity = arr[1]
        
    weights = [int(x) for x in input().split()]
    vals =[int(x) for x in input().split()]
        
    sol = Solution()
    res = sol.knapsack(mat_size, capacity,weights,vals)
        
    print(res)   
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n)
<br>
![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id="416"><a href="https://leetcode.com/problems/partition-equal-subset-sum">416. Partition Equal Subset Sum</a></h2><h3>Medium</h3><p>Given an integer array <code>nums</code>, return <code>true</code> <em>if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,11,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned as [1, 5, 5] and [11].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array cannot be partitioned into equal sum subsets.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


### Solving approach:  


![0-1 knapsack-416](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day42/Leetcode416-thought.jpg)


 
### My Solution 2：_`xxx`_  

  
```python

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False  
        
        target = sum(nums) //2

        dp = [0] * (target + 1)

        for num in nums:
            for j in range(target, num -1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        
        return dp[-1] == target

        
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2)
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




