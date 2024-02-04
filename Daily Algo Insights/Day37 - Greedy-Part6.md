# Day37 Greedy Part 6


## Contents
* **[738. Monotone Increasing Digits](#738)**
* **[968. Binary Tree Cameras](#968)**


<br>
<h2 id = "738"><a href="https://leetcode.com/problems/monotone-increasing-digits">738. Monotone Increasing Digits</a></h2><h3>Medium</h3><p>An integer has <strong>monotone increasing digits</strong> if and only if each pair of adjacent digits <code>x</code> and <code>y</code> satisfy <code>x &lt;= y</code>.</p>

<p>Given an integer <code>n</code>, return <em>the largest number that is less than or equal to </em><code>n</code><em> with <strong>monotone increasing digits</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1234
<strong>Output:</strong> 1234
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 332
<strong>Output:</strong> 299
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


![Thought process - Q738](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day37/Leetcode738-thought.jpg)



### My Solution 1：

  
```python

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        n_list = list(str(n))
        
        # 从后向前list(size, x + 1 = 实际停止位置， -1)
        for i in range(len(n_list)-1,0,-1):
            if n_list[i-1] > n_list[i]:
                n_list[i-1] = str(int(n_list[i-1]) - 1)
                n_list[i:] = "9" * (len(n_list) - i)

        #最后除了拼接成string 还需要转成 integer
        return int("".join(n_list))
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(d) where d is the number of digits in 'n'.
  
- *`Space Complexity`*:<br>
O(d)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "968"><a href="https://leetcode.com/problems/binary-tree-cameras">968. Binary Tree Cameras</a></h2><h3>Hard</h3><p>You are given the <code>root</code> of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.</p>

<p>Return <em>the minimum number of cameras needed to monitor all nodes of the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png" style="width: 138px; height: 163px;" />
<pre>
<strong>Input:</strong> root = [0,0,null,0,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> One camera is enough to monitor all nodes if placed as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png" style="width: 139px; height: 312px;" />
<pre>
<strong>Input:</strong> root = [0,0,null,0,null,0,null,null,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>Node.val == 0</code></li>
</ul>



### Solving approach 1:


![Thought process - Q968-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day37/Leetcode968-thought_1.jpg)
![Thought process - Q968-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day37/Leetcode968-thought_2.jpg)


### My Solution 1：_`Greedy postorder `_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #后序遍历
        res = 0
        
        def postorder(cur_node):
            # Declare res as nonlocal to modify it within this function
            nonlocal res
            # base case
            if not cur_node: 
                return 2
            
            left = postorder(cur_node.left)
            right = postorder(cur_node.right)

            if left==2 and right == 2:
                return 0
            
            if left == 0 or right == 0:
                res += 1
                return 1
            
            if left == 1 or right == 1:
                return 2

        # 内部调用必须在定义后面
        # case 4 root is not covered
        if postorder(root) == 0:
            res += 1
        return res
        
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of nodes in the binary tree
  
- *`Space Complexity`*:<br>
O(n), O(h) can be average case , where h is the height of the tree. 
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx



