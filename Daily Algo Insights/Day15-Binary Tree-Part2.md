# Dayxx - xxxxxx


## Contents
* **[102.Binary Tree Level Order Traversal](#102)**
* **[107](#)**
* **[199](#)**
* **[637](#)**
* **[429](#)**
* **[515](#xxx)**
* **[116](#)**
* **[117](#)**
* **[104](#)**
* **[111](#)**
* **[226](#xxx)**
* **[101](#)**


<br>
![Day 15](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day15/Day15.png)
<br>
<h2 id = "102"><a href="https://leetcode.com/problems/binary-tree-level-order-traversal">102. Binary Tree Level Order Traversal</a></h2><h3>Medium</h3><p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>



### My Solution 1：_`deque + level /BFS`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:

            level = []
            queue_size = len(queue)

            for _ in range(queue_size):
                node = queue.popleft()
                level.append(node.val)

                # for child in (node.left,node.right):
                #     if child:
                #         queue.append(child)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            res.append(level)

        return res
                        



```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
---

![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png）










