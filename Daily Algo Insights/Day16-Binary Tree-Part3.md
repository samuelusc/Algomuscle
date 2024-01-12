# Day16 - Binary Tree Part 3


## Contents
* **[104.Maximum Depth of Binary Tree](#104)**
* **[111.Minimum Depth of Binary Tree](#111)**
* **[222.Count Complete Tree Nodes](#222)**

![Day 16](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day16/Day16.png)

## Key Points


- **Height** `高度指的是任一节点到叶节点的距离`， 从根节点到叶节点的距离就是树的高度。另外叶节点本身的高度在习题中如Leetcode视为1，但也有视为0的，那么他们的返回值也有所不同（return 0 or return -1)

- **Depth** `深度指的是任一节点到根节点的距离`，从叶子节点到根节点的距离就是深度。 这个概念在同时具备（根节点，叶子节点）两个条件时，Depth and Height 是一样的。另外同样习题中多把root 根节点本身的深度视作1，但也可以为0：(return 0, reutrn -1)


---



<h2><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree">104. Maximum Depth of Binary Tree</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary tree, return <em>its maximum depth</em>.</p>

<p>A binary tree&#39;s <strong>maximum depth</strong>&nbsp;is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


### My Solution 1：_`Iteration Level traversal`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        res = 0

        queue = deque([root])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res += 1
        
        return res
            



        
```


---


### My Solution 2：_`Step by step (Post-order recursion)`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #post-order traversal
        if not root:
            return 0

        # 计算左孩子
        leftHeight = self.maxDepth(root.left)

        #计算右孩子
        rightHeight = self.maxDepth(root.right)

        #返回给父节点
        # 1 是它本身 + 最大返回值
        result = 1 +  max(leftHeight, rightHeight)

        return result

```


---

 
### My Solution 3：_`concise recursion(post-order)`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
```


**Complexity Analysis:**  

- *`Time Complexity`*:

  
- *`Space Complexity`*:

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "111"><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree">111. Minimum Depth of Binary Tree</a></h2><h3>Easy</h3><p>Given a binary tree, find its minimum depth.</p>

<p>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [2,null,3,null,4,null,5,null,6]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>5</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>



### My Solution 1：_`Iteration`_  

  
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node, depth = queue.popleft()
                # 检查是否到达叶节点
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    queue.append((node.left, depth + 1))
                
                if node.right:
                    queue.append((node.right, depth + 1))



```

---


### My Solution 2：_`step by Step (Post-order Recursion)`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #通过高度计算深度
        #后续遍历-递归
        if not root:
            #查看例题root 深度1or0
            return 0 #root 深度1

        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        #区别于Max depth
        #判断是否一侧为空
        if not leftHeight and rightHeight:
            return 1 + rightHeight

        if not rightHeight and leftHeight:
            return 1 + leftHeight
        # 后序遍历: 左右中
        return 1 + min(leftHeight,rightHeight)
```


---

  
### My Solution 2：_`concise Recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 如果没有左子树，则计算右子树高度
        if not root.left:
            return 1 + self.minDepth(root.right)
        # 如果没有右子树，则计算左子树高度
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "222"><a href="https://leetcode.com/problems/count-complete-tree-nodes">222. Count Complete Tree Nodes</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a <strong>complete</strong> binary tree, return the number of the nodes in the tree.</p>

<p>According to <strong><a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a></strong>, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between <code>1</code> and <code>2<sup>h</sup></code> nodes inclusive at the last level <code>h</code>.</p>

<p>Design an algorithm that runs in less than&nbsp;<code data-stringify-type="code">O(n)</code>&nbsp;time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code></li>
	<li>The tree is guaranteed to be <strong>complete</strong>.</li>
</ul>


### My Solution 1：_`Iteration`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # implement stack to compute the number of nodes
        if not root:
            return 0
        
        res = 0
        stack = [root]
        
        while stack:
            level_size = len(stack)

            for _ in range(level_size):
                node = stack.pop()
                res += 1

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return res
```

---

 
### My Solution 2：_`Recursion-Post`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Post-Order traversal

        # 结束条件
        if not root:
            return 0
        #左子树
        left_count = self.countNodes(root.left)
        #右子树
        right_count = self.countNodes(root.right)
        #中节点
        result = left_count + right_count + 1

        return result
```
---

### My Solution 3：_`implement Complete Binary Tree Property`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # implement the properties of complete binary tree
        #终止条件1
        if not root:
            return 0

        level = 1 #root is counted as 1
        left,right = root.left, root.right

        while left and right:
            level += 1
            left,right = left.left, right.right
        
        # 叶节点之后
        if not left and not right:
            # 节点数 = 2 ** level - 1 (1base)
            #终止条件2
            return 2 ** level - 1
        
        # post order traversal to count the numbers of nodes 
        # 单层递归逻辑
        leftNums = self.countNodes(root.left)
        rightNums = self.countNodes(root.right)
        result = leftNums + rightNums + 1
        return result

        # return self.countNodes(root.left) + self.countNodes(root.right) + 1
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)










