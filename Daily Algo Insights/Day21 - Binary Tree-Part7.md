# Day21 - Binary Tree Part 7


## Contents
* **[530.Minimum Absolute Difference in BST](#530)**
* **[501.Find Mode in Binary Search Tree](#501)**
* **[236.Lowest Common Ancestor of a Binary Tree](#236)**


<br>
<h2 id = "530"><a href="https://leetcode.com/problems/minimum-absolute-difference-in-bst">530. Minimum Absolute Difference in BST</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a Binary Search Tree (BST), return <em>the minimum absolute difference between the values of any two different nodes in the tree</em>.</p>

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


<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "501"><a href="https://leetcode.com/problems/find-mode-in-binary-search-tree">501. Find Mode in Binary Search Tree</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary search tree (BST) with duplicates, return <em>all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (i.e., the most frequently occurred element) in it</em>.</p>

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


<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)





<h2 id = "236"><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree">236. Lowest Common Ancestor of a Binary Tree</a></h2><h3>Medium</h3><p>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The LCA of nodes 5 and 1 is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation:</strong> The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2], p = 1, q = 2
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> will exist in the tree.</li>
</ul>



### My Solution 1：_`postorder Recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # post-order -> left, right , root

        # base case: if current node is None,return None
        if not root:
            return None
        # base case: if current node matches either p or q,
        # return current node
        if root == p or root == q:
            return root

        # recursively search in the left / right subtree for p or q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # handling 4 cases based on the nodes
        # found in the left and right subtress

        # Case1:if left and right subtree are not None
        # means the current node is their lowest common ancestor
        if left and right:
            return root

        # Case 2: If both left and right are None,
        # it means neither p nor q are found in the subtree of the cur node
        if not left and not right:
            return None

        # Case3: either p or q found in the left subtree
        elif left:
            return left
        # Case4: either p or q found in the right subtree
        else:
            return right
```


- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(h) where h is the height of the tree
---

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
