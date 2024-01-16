# Dayxx - Binary Tree Part 7


## Contents
* **[530.Minimum Absolute Difference in BST](#530)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**

<br>
<h2 id = "530"><a href="https://leetcode.com/problems/minimum-absolute-difference-in-bst">530. Minimum Absolute Difference in BST</a></h2><h3>Easy</h3><hr><p>Given the <code>root</code> of a Binary Search Tree (BST), return <em>the minimum absolute difference between the values of any two different nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [4,2,6,1,3]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [1,0,48,null,null,12,49]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 783: <a href="https://leetcode.com/problems/minimum-distance-between-bst-nodes/" target="_blank">https://leetcode.com/problems/minimum-distance-between-bst-nodes/</a></p>
<br>

### Solving approach 1:


- BST 遍历首先要想到`中序遍历` -> `单调递增`



### My Solution 1：_`inorder- recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # inorder traversal
        # BST 单调递增->中序遍历

        res = float('inf')
        pre_node = None

        def inorder(cur_node):
            # base case 
            if not cur_node:
                return 
            # 左子树递归
            inorder(cur_node.left)

            #define immutable variable global
            nonlocal res, pre_node

            # 处理中间节点
            if pre_node:
                res = min(res, cur_node.val - pre_node.val)
            # previous node 指向current node
            pre_node = cur_node
            
            # 右子树递归 
            inorder(cur_node.right)

        inorder(root)
        return res


```


- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n)
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "501"><a href="https://leetcode.com/problems/find-mode-in-binary-search-tree">501. Find Mode in Binary Search Tree</a></h2><h3>Easy</h3><hr><p>Given the <code>root</code> of a binary search tree (BST) with duplicates, return <em>all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (i.e., the most frequently occurred element) in it</em>.</p>

<p>If the tree has more than one mode, return them in <strong>any order</strong>.</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than or equal to</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than or equal to</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).




### My Solution 1：_`xxx`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.count = 0
        self.max_count = 0
        self.pre_node = None

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder traversal

        # Base case: return if node is None
        if not root:
            return

        # Traverse the left subtree
        self.findMode(root.left)

        # Process the current node
        # Assign count as 1 if previous node is None
        if not self.pre_node:
            self.count = 1
        # Increment count if current node value equals previous node value
        elif self.pre_node.val == root.val:
            self.count += 1
        # Reset count to 1 if current node value is different
        else:
            self.count = 1

        # Update previous node to the current node
        self.pre_node = root

        # If count equals max_count, add current node value to res
        if self.count == self.max_count:
            self.res.append(root.val)
        # If count is greater than max_count, reset res and update max_count
        elif self.count > self.max_count:
            self.max_count = self.count
            self.res = [root.val]

        # Traverse the right subtree
        self.findMode(root.right)
        # Return the list of mode(s)
        return self.res
```


- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n)
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



