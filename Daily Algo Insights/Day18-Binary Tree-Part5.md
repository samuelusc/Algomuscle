# Day15 - Day18 Binary Tree Part 5

### [Study Reference](https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html)  

## Contents
* **[513.Find Bottom Left Tree Value](#513)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
<br>
xxximagexxx
<br>
<h2 id = "513"><a href="https://leetcode.com/problems/find-bottom-left-tree-value">513. Find Bottom Left Tree Value</a></h2><h3>Medium</h3><hr><p>Given the <code>root</code> of a binary tree, return the leftmost value in the last row of the tree.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg" style="width: 432px; height: 421px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,null,5,6,null,null,7]
<strong>Output:</strong> 7
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


xxxx


### My Solution 1：_`recursion (step by step)`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not neccesary the left child,but the leftmost value in the bottom
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #initialzie the result and minDepth
        # 设为实例属性
        self.result = 0
        self.minDepth = float("-inf")

        return self.traversal(root, 0)


    def traversal(self, node, depth):
        # Base case: if the node is a leaf node
        if not node.left and not node.right:
            # Update the result and minDepth
            if depth > self.minDepth:
                self.minDepth = depth
                self.result = node.val
        #If the node has a left child traversae left subtree
        # 先左后右   
        if node.left:
            depth += 1
            self.traversal(node.left,depth)
            #backtracking step , decrement depth
            depth -= 1

        #If the node has a right child    
        if node.right:
            depth += 1
            self.traversal(node.right,depth)
            depth -= 1
        
        return self.result
```

---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`iteration-deque`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Constrain 保证至少有一个node
        # 注意！ 层级遍历要用queue 而不是 stack     
        queue = deque([root])
    
        while queue:
            level_size = len(queue)

            # 取每行第一个node.val
            for i in range(level_size):
                node = queue.popleft()

                # 将第一个node.val 赋给 left_most
                if i == 0:
                    leftmost = node.val
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost
```


**Complexity Analysis:**  

- *`Time Complexity`*:

  
- *`Space Complexity`*:

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



xxxx







