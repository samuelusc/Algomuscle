# Day15 - Day18 Binary Tree Part 5




## Contents
* **[513.Find Bottom Left Tree Value](#513)**
* **[112.Path Sum](#112)**
* **[106.Construct Binary Tree from Inorder and Postorder Traversal](#106)**

<br>
<h2 id = "513"><a href="https://leetcode.com/problems/find-bottom-left-tree-value">513. Find Bottom Left Tree Value</a></h2><h3>Medium</h3><p>Given the <code>root</code> of a binary tree, return the leftmost value in the last row of the tree.</p>

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

### My Solution 2：_`concise Recurison`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = float("-inf")
        self.res = None
        self.traversal(root, 0)
        return self.res

    def traversal(self, root, depth):
        if not root.left and not root.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = root.val
            
        if root.left:
            self.traversal(root.left, depth + 1)

        if root.right:
            self.traversal(root.right, depth + 1)
```


---
 
### My Solution 3：_`iteration-deque`_  

  
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
O(n)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "112"><a href="https://leetcode.com/problems/path-sum">112. Path Sum</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <code>true</code> if the tree has a <strong>root-to-leaf</strong> path such that adding up all the values along the path equals <code>targetSum</code>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>Output:</strong> true
<strong>Explanation:</strong> The root-to-leaf path with the target sum is shown.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />
<pre>
<strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> false
<strong>Explanation:</strong> There two root-to-leaf paths in the tree:
(1 --&gt; 2): The sum is 3.
(1 --&gt; 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [], targetSum = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> Since the tree is empty, there are no root-to-leaf paths.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>



### My Solution 1：_`recursion (step by step)`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # self.traversal(root, target) is incorrect such as
        # ([1],1)
        return self.traversal(root, targetSum - root.val)

    def traversal(self, root, count):
        if not root.left and not root.right:
            return count == 0

        if root.left:
            count -= root.left.val
            if self.traversal(root.left, count):
                return True
            count += root.left.val

        if root.right:
            count -= root.right.val
            if self.traversal(root.right, count):
                return True
            count += root.right.val

        return False
        


        
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sumNode):
            if not root:
                return False
            
            sumNode += root.val

            if not root.left and not root.right and sumNode == targetSum:
                return True

            return dfs(root.left, sumNode) or dfs(root.right, sumNode)
        
        return dfs(root, 0)
        


        
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id= "106"><a href="https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal">106. Construct Binary Tree from Inorder and Postorder Traversal</a></h2><h3>Medium</h3><p>Given two integer arrays <code>inorder</code> and <code>postorder</code> where <code>inorder</code> is the inorder traversal of a binary tree and <code>postorder</code> is the postorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> inorder = [-1], postorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= inorder.length &lt;= 3000</code></li>
	<li><code>postorder.length == inorder.length</code></li>
	<li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li>
	<li><code>inorder</code> and <code>postorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>postorder</code> also appears in <code>inorder</code>.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
	<li><code>postorder</code> is <strong>guaranteed</strong> to be the postorder traversal of the tree.</li>
</ul>







### Solving approach 1:

- 关键点在于先在postorder中找到 `root value` -> `postorder[-1]`

- 在inorder中找到 root 的索引 index, 这样就把这课inorder树分为了 [: index] index [index+1: ] 三部分

- 由于postorder 存在·左子树永远在右子树前面·的性质，而 inorder 树的左半部分同样也是 postorder 的左半部分(同样的数量-> `inorder[:i] 和 postorder[:i] 有相同元素`

- 同理 `inorder[i+1:] 和 postorder[i:-1]`  也具有相同的右子树元素


### My Solution 1：_`recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(val=root_val)

        index = inorder.index(root_val)
        # 中序遍历的根节点index也是后序遍历左右结点的分界
        root.left = self.buildTree(inorder[:index],postorder[:index])
        
        root.right = self.buildTree(inorder[index + 1:],postorder[index: -1])
        return root
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n^2), since .index() clled on the inorder list takes O(n) and will call buildTree n times.
  
- *`Space Complexity`*:
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)


