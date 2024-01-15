# Day19 - Binary Tree Part6.md


## Contents
* **[654.Maximum Binary Tree](#654)**
* **[617.Merge Two Binary Trees](#617)**
* **[700.Search in a Binary Search Tree](#700)**
* **[xx](#)**
* **[xx](#)**

<br>
<h2 id = "654"><a href="https://leetcode.com/problems/maximum-binary-tree">654. Maximum Binary Tree</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> with no duplicates. A <strong>maximum binary tree</strong> can be built recursively from <code>nums</code> using the following algorithm:</p>

<ol>
	<li>Create a root node whose value is the maximum value in <code>nums</code>.</li>
	<li>Recursively build the left subtree on the <strong>subarray prefix</strong> to the <strong>left</strong> of the maximum value.</li>
	<li>Recursively build the right subtree on the <strong>subarray suffix</strong> to the <strong>right</strong> of the maximum value.</li>
</ol>

<p>Return <em>the <strong>maximum binary tree</strong> built from </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg" style="width: 302px; height: 421px;" />
<pre>
<strong>Input:</strong> nums = [3,2,1,6,0,5]
<strong>Output:</strong> [6,3,5,null,2,0,null,null,1]
<strong>Explanation:</strong> The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg" style="width: 182px; height: 301px;" />
<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [3,null,2,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All integers in <code>nums</code> are <strong>unique</strong>.</li>
</ul>

### Solving approach 1:

- 构建树：首先想到`前序遍历`，先找到`root value` 建立树的根节点，再根据根节点在数组中的`index`划分左右子树，再`分别递归`找到它们的根节点，并建立相应的子树


### My Solution 1：_`preorder-Step by step`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 构建树->前序遍历
        # base case,递归结束条件
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_value, index = 0, 0
        # 数组中找到root
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                index = i
        # 建立根
        node = TreeNode(max_value)
        
        #保证左子树至少有一个元素
        if index > 0:
            new_nums = nums[:index]
            #递归调用的结果来构建左子树
            node.left = self.constructMaximumBinaryTree(new_nums)
        
        # nums.size -1 保证至少右子树有一个元素
        if index < len(nums)-1:
            new_nums = nums[index+1:]
            node.right = self.constructMaximumBinaryTree(new_nums)
        
        # 返回根节点
        return node
```

### My Solution 2：_`concise Preorder`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 尽管 nums.size >= 1,但是递归后的数组有可能是空的
        # 检查nums是否为空
        if not nums:
            return None
        root = max(nums)
        index = nums.index(root)

        # 建立树的根节点
        node = TreeNode(root)    

        # 如果列表为空，递归会在 if not nums 时处理
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])

        return node
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n^2)
  
- *`Space Complexity`*:
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "617"><a href="https://leetcode.com/problems/merge-two-binary-trees">617. Merge Two Binary Trees</a></h2><h3>Easy</h3><hr><p>You are given two binary trees <code>root1</code> and <code>root2</code>.</p>

<p>Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.</p>

<p>Return <em>the merged tree</em>.</p>

<p><strong>Note:</strong> The merging process must start from the root nodes of both trees.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/merge.jpg" style="width: 600px; height: 163px;" />
<pre>
<strong>Input:</strong> root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
<strong>Output:</strong> [3,4,5,5,4,null,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root1 = [1], root2 = [1,2]
<strong>Output:</strong> [2,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both trees is in the range <code>[0, 2000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>



### My Solution 1：_`preOrder-inplace`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Pre-order

        # base case 终止条件
        # 处理树为空的情况
        if not root1:
            return root2
        if not root2:
            return root1
        #合并根节点
        root1.val += root2.val
        #新树的左右节点（用了原来的树结构）
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
```


- *`Time Complexity`*:
O(n) where n is the number of nodes in the smaller tree between root1 and root2
  
- *`Space Complexity`*:
O(n) where n is the height of the smaller tree. Worst case can be O(min(n1,n2)) where the height of smaller tree is same as its number of nodes. Best case is log(min(n1,n2)) in balanced binary tree.
---
  

 
### My Solution 2：_`construct new tree`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #construct a new binary tree

        if not root1:
            return root2
        
        if not root2:
            return root1

        merge_node = TreeNode(root1.val + root2.val)

        merge_node.left = self.mergeTrees(root1.left, root2.left)
        merge_node.right = self.mergeTrees(root1.right, root2.right)

        return merge_node
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n) where n is the number of nodes in the smaller tree between root1 and root2
  
- *`Space Complexity`*:
O(m+n), where m and n are the number of nodes in root1 and root2.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "700"><a href="https://leetcode.com/problems/search-in-a-binary-search-tree">700. Search in a Binary Search Tree</a></h2><h3>Easy</h3><hr><p>You are given the <code>root</code> of a binary search tree (BST) and an integer <code>val</code>.</p>

<p>Find the node in the BST that the node&#39;s value equals <code>val</code> and return the subtree rooted with that node. If such a node does not exist, return <code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" style="width: 422px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 2
<strong>Output:</strong> [2,1,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" style="width: 422px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 5000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>7</sup></code></li>
	<li><code>root</code> is a binary search tree.</li>
	<li><code>1 &lt;= val &lt;= 10<sup>7</sup></code></li>
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如过树为空，或树的根节点就是 target value
        if not root or root.val == val:
            return root
        #initialize res to None
        res = None

        # 当根节点value > target value时
        if root.val > val:
            #将查找结果存入res
            res = self.searchBST(root.left, val)

        else:
            res = self.searchBST(root.right, val)

        return res
```


- *`Time Complexity`*:
O(h) where h is the hight of the BST tree.

  
- *`Space Complexity`*:
O(h) depends on the depth of recursion which is related to the hight(h) of the tree.\
---
  

### My Solution 2：_`stack`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 使用单独变量，不会改变原始树的结构root 指针
        cur = root

        while cur:
            if cur.val > val:
                cur = cur.left
            
            elif cur.val < val:
                cur = cur.right
            
            else:
                return cur
        #没找到返回None
        return None
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(h) where h is the hight of the BST tree.
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



xxxx




