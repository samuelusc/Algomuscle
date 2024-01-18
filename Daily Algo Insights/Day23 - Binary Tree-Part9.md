# Day23 - Binary Tree Part 9


## Contents
* **[669.Trim a Binary Search Tree](#669)**
* **[108.Convert Sorted Array to Binary Search Tree](#108)**
* **[538.Convert BST to Greater Tree](#538)**



<br>
<h2 id ="669"><a href="https://leetcode.com/problems/trim-a-binary-search-tree">669. Trim a Binary Search Tree</a></h2><h3>Medium</h3><p>Given the <code>root</code> of a binary search tree and the lowest and highest boundaries as <code>low</code> and <code>high</code>, trim the tree so that all its elements lies in <code>[low, high]</code>. Trimming the tree should <strong>not</strong> change the relative structure of the elements that will remain in the tree (i.e., any node&#39;s descendant should remain a descendant). It can be proven that there is a <strong>unique answer</strong>.</p>

<p>Return <em>the root of the trimmed binary search tree</em>. Note that the root may change depending on the given bounds.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg" style="width: 450px; height: 126px;" />
<pre>
<strong>Input:</strong> root = [1,0,2], low = 1, high = 2
<strong>Output:</strong> [1,null,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg" style="width: 450px; height: 277px;" />
<pre>
<strong>Input:</strong> root = [3,0,4,null,2,null,null,1], low = 1, high = 3
<strong>Output:</strong> [3,2,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The value of each node in the tree is <strong>unique</strong>.</li>
	<li><code>root</code> is guaranteed to be a valid binary search tree.</li>
	<li><code>0 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code></li>
</ul>

### My Solution 1：_`recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        #base case
        if not root:
            return 
        #处理当前节点
        # 当前根节点<low, 去查看它的右子树找到符合 >= low 的并返回
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # 当前节点>hight, 去查看左子树 
        if root.val > high:
            return self.trimBST(root.left, low, high)


        # root.left 连接递归后的左节点
        root.left = self.trimBST(root.left, low, high)
        # root.right 连接递归后的右节点
        root.right = self.trimBST(root.right, low, high)
        #返回trimed root
        return root
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(h), where h is the height of the binary tree. O(logn - n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "108"><a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree">108. Convert Sorted Array to Binary Search Tree</a></h2><h3>Easy</h3><p>Given an integer array <code>nums</code> where the elements are sorted in <strong>ascending order</strong>, convert <em>it to a </em><span data-keyword="height-balanced"><strong><em>height-balanced</em></strong></span> <em>binary search tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;" />
<pre>
<strong>Input:</strong> nums = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;" />
<pre>
<strong>Input:</strong> nums = [1,3]
<strong>Output:</strong> [3,1]
<strong>Explanation:</strong> [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in a <strong>strictly increasing</strong> order.</li>
</ul>




### My Solution 1：_`recursion-middle`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.traversal(nums, 0, len(nums) -1)

    # 构造平衡二叉搜索树要从递增数组的中间选root
    # 递归构造 bst    
    def traversal(self, nums, left, right):
        if left > right:
            return

        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        root.left = self.traversal(nums, left, mid -1)
        root.right = self.traversal(nums, mid + 1, right)

        return root
    
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of elements in the input list nums.
  
- *`Space Complexity`*:<br>
O(n), best case: o(logn)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "538"><a href="https://leetcode.com/problems/convert-bst-to-greater-tree">538. Convert BST to Greater Tree</a></h2><h3>Medium</h3><p>Given the <code>root</code> of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.</p>

<p>As a reminder, a <em>binary search tree</em> is a tree that satisfies these constraints:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/02/tree.png" style="width: 500px; height: 341px;" />
<pre>
<strong>Input:</strong> root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
<strong>Output:</strong> [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [0,null,1]
<strong>Output:</strong> [1,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>All the values in the tree are <strong>unique</strong>.</li>
	<li><code>root</code> is guaranteed to be a valid binary search tree.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1038: <a href="https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/" target="_blank">https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/</a></p>





### My Solution 1：_`stack-template`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stack 模版-> 右中左 
        stack = []
        pre_val = 0
        cur_node = root

        while stack or cur_node:
            if cur_node:
                stack.append(cur_node)
                #遍历右
                cur_node = cur_node.right

            else:
                # 中处理
                cur_node = stack.pop()
                cur_node.val += pre_val
                pre_val = cur_node.val
                # 遍历左
                cur_node = cur_node.left
        
        return root

```


- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n)
---
  

 
### My Solution 2：_`recursion Reversed inorder`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Two pointers 
        #inorder -> 到序遍历 右->中->左
       
        # previou val 设为0不改变最大值
        # 不设置pre_node 是避免None 情况
        self.pre_val = 0

        return self.traversal(root)
    

    def traversal(self, cur_node):
        if not cur_node:
            return 

        # right
        self.traversal(cur_node.right)

        # process root
        cur_node.val += self.pre_val
        self.pre_val = cur_node.val

        # left
        self.traversal(cur_node.left)
        
        return cur_node
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n)
  
- *`Space Complexity`*:<br>
O(n). The space complexity is determined by the depth of the recursive call stack in the traversal
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>







