# Day17 - Binary Tree-Part4



## Contents
* **[110.Balanced Binary Tree](#110)**
* **[257.Binary Tree Paths](#257)**
* **[404.Sum of Left Leaves](#404)**


<br>
<h2 id ="110"><a href="https://leetcode.com/problems/balanced-binary-tree">110. Balanced Binary Tree</a></h2><h3>Easy</h3><p>Given a binary tree, determine if it is <span data-keyword="height-balanced"><strong>height-balanced</strong></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>



### My Solution 1：_`xxx`_  

  
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) != -1:
            return True
        else:
            return False


    def getHeight(self, root:TreeNode) -> int:
        # base case 递归结束条件
        if not root:
            return 0

        # 单层递归逻辑
        # 左子树不平衡 = -1
        leftHeight = self.getHeight(root.left) 
        if leftHeight == -1:
            return -1
        
        # 右子树不平衡 = -1
        rightHeight = self.getHeight(root.right) 
        if rightHeight == -1:
            return -1
        
        # 父节点汇总 （中）
        if abs(leftHeight - rightHeight) > 1:
            return -1 
        else:
            return 1 + max(leftHeight, rightHeight)
    
        

        

```

**Complexity Analysis:**  

- *`Time Complexity`*:

  
- *`Space Complexity`*:

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "257"><a href="https://leetcode.com/problems/binary-tree-paths">257. Binary Tree Paths</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary tree, return <em>all root-to-leaf paths in <strong>any order</strong></em>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,5]
<strong>Output:</strong> [&quot;1-&gt;2-&gt;5&quot;,&quot;1-&gt;3&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [&quot;1&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


xxxx


### My Solution 1：_`xxx`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 前序遍历
        path = []
        result = []
        if not root:
            return result
        self.dfs(root, path, result)
        return result
    

    def dfs(self, cur_node, path, result):
        # 父节点 （中）
        path.append(cur_node.val)
        # 到达叶子节点
        if not cur_node.left and not cur_node.right:
            result.append('->'.join(map(str,path)))
            return 

        if cur_node.left:
            self.dfs(cur_node.left, path, result)
            path.pop()
        
        if cur_node.right:
            self.dfs(cur_node.right, path, result)
            path.pop()


    
```

**Complexity Analysis:**  

- *`Time Complexity`*:

  
- *`Space Complexity`*:

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id ="404"><a href="https://leetcode.com/problems/sum-of-left-leaves">404. Sum of Left Leaves</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary tree, return <em>the sum of all left leaves.</em></p>

<p>A <strong>leaf</strong> is a node with no children. A <strong>left leaf</strong> is a leaf that is the left child of another node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 24
<strong>Explanation:</strong> There are two left leaves in the binary tree, with values 9 and 15 respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


xxxx


### My Solution 1：_`xxx`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        leftValue = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            leftValue = root.left.val

        rightValue = self.sumOfLeftLeaves(root.right)

        sum_val = leftValue + rightValue

        return sum_val 
```

**Complexity Analysis:**  

- *`Time Complexity`*:

  
- *`Space Complexity`*:

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



xxxx







