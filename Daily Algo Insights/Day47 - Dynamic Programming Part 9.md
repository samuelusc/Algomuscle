# Day47 - Dynamic Programming Part 9


## Contents
* **[198. House Robber](#198)**
* **[213. House Robber II](#213)**
* **[337. House Robber III](#337)**

<br>

<br>

<h2 id = "198"><a href="https://leetcode.com/problems/house-robber">198. House Robber</a></h2><h3>Medium</h3><p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![198-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day47/LC198-thoght.jpg)


### My Solution 1：  

  
```python

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0] 
        dp[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])


        return dp[-1]
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the length of the input list nums
  
- *`Space Complexity`*:<br>
O(n), where n is the length of nums

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "213"><a href="https://leetcode.com/problems/house-robber-ii">213. House Robber II</a></h2><h3>Medium</h3><p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


### Solving approach 1:


![213 thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day47/LC213-thought.jpg)


### My Solution 1：_`regular`_  

  
```python

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        


        def helper(new_nums):
            if len(new_nums) < 2:
                return new_nums[0]

            dp = [0] * len(new_nums)    
            dp[0] = new_nums[0]
            dp[1] = max(new_nums[0],new_nums[1])

            for i in range(2, len(new_nums)):
                dp[i] = max(dp[i-1],dp[i-2] + new_nums[i])
            
            return dp[-1]
        
        res = max(helper(nums[1:]), helper(nums[:-1]))
        return res


    
```


- *`Time Complexity`*:<br>
O(n)

Since each call to helper has a complexity of O(n-1) and there are two such calls, the overall time complexity is O(2*(n-1)) 
  
- *`Space Complexity`*:<br>
O(n)
---
  

 
### My Solution 2：_`save space`_  

  
```python

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        


        def helper(nums, start, end):
            if start == end:
                return nums[start]
            
            pre = nums[start]
            cur = max(nums[start],nums[start + 1])

            for i in range(start + 2, end + 1):
                temp = cur
                cur = max(pre + nums[i], temp)
                pre = temp
            
            return cur
           
        
        res = max(helper(nums, 0, len(nums) -2), helper(nums, 1, len(nums)-1))
        return res


    
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)

  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "337"><a href="https://leetcode.com/problems/house-robber-iii">337. House Robber III</a></h2><h3>Medium</h3><p>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called <code>root</code>.</p>

<p>Besides the <code>root</code>, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if <strong>two directly-linked houses were broken into on the same night</strong>.</p>

<p>Given the <code>root</code> of the binary tree, return <em>the maximum amount of money the thief can rob <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg" style="width: 277px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [3,2,3,null,3,null,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg" style="width: 357px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,3,null,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 4 + 5 = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>



### Solving approach:  


![337-thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day47/LC337-thought.jpg)
 
### My Solution：_`dp + postorder traversal`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.robTree(root)
        return max(res[0],res[1])


    def robTree(self, cur_node):
        if not cur_node:
            return [0,0]

        leftDp = self.robTree(cur_node.left)
        rightDp = self.robTree(cur_node.right)

        val1 = cur_node.val + leftDp[0] + rightDp[0]
        val2 = max(leftDp[0],leftDp[1]) + max(rightDp[0],rightDp[1])

        return [val2,val1]    
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of nodes in the binary tree.
  
- *`Space Complexity`*:<br>
O(n), due to the depth of the recursive call stack.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>





