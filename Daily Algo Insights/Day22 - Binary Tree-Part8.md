# Day22 - Binary Tree Part 8



## Contents
* **[235.Lowest Common Ancestor of a Binary Search Tree](#235)**
* **[701.Insert into a Binary Search Tree](#701)**
* **[450.Delete Node in a BST](#450)**



<br>
<h2 id = "235"><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree">235. Lowest Common Ancestor of a Binary Search Tree</a></h2><h3>Medium</h3><p>Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow <strong>a node to be a descendant of itself</strong>).&rdquo;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;" />
<pre>
<strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> The LCA of nodes 2 and 8 is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;" />
<pre>
<strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [2,1], p = 2, q = 1
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> will exist in the BST.</li>
</ul>
### Breakdown and Thought Process:  
<br>


### My Solution 1：_`recursion - Step by step`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traversal(root, p, q)
    
    def traversal(self, cur_node, p, q):
        if not cur_node:
            return 
        
        if cur_node.val > p.val and cur_node.val > q.val:
            left = self.traversal(cur_node.left, p, q)
            if left: return left
        
        if cur_node.val < p.val and cur_node.val < q.val:
            right = self.traversal(cur_node.right, p, q)
            if right: return right
        
        return cur_node
```


- *`Time Complexity`*:<br>
O(n)

- *`Space Complexity`*:<br>
O(h), where h is the height of teh tree, due to the recursive stack. (O(n) in the worst case and O(logn) in the best case)
  

 
### My Solution 2：_`iteration`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_node = root
        
        while cur_node:
            if cur_node:
                if cur_node.val > p.val and cur_node.val > q.val:
                    cur_node = cur_node.left

                elif cur_node.val < p.val and cur_node.val < q.val:
                    cur_node = cur_node.right
            
                else:
                    return cur_node
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(h),where h is the height of the binary tree. THe height h could be linear in respect to the number of nodes N.

  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "701"><a href="https://leetcode.com/problems/insert-into-a-binary-search-tree">701. Insert into a Binary Search Tree</a></h2><h3>Medium</h3><p>You are given the <code>root</code> node of a binary search tree (BST) and a <code>value</code> to insert into the tree. Return <em>the root node of the BST after the insertion</em>. It is <strong>guaranteed</strong> that the new value does not exist in the original BST.</p>

<p><strong>Notice</strong>&nbsp;that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg" style="width: 752px; height: 221px;" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> [4,2,7,1,3,5]
<strong>Explanation:</strong> Another accepted tree is:
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/bst.jpg" style="width: 352px; height: 301px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [40,20,60,10,30,50,70], val = 25
<strong>Output:</strong> [40,20,60,10,30,50,70,null,null,25]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
<strong>Output:</strong> [4,2,7,1,3,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in&nbsp;the tree will be in the range <code>[0,&nbsp;10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>8</sup> &lt;= Node.val &lt;= 10<sup>8</sup></code></li>
	<li>All the values <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>-10<sup>8</sup> &lt;= val &lt;= 10<sup>8</sup></code></li>
	<li>It&#39;s <strong>guaranteed</strong> that <code>val</code> does not exist in the original BST.</li>
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        # 注意这部分要比较的是root.val not root.left.val
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root
```


- *`Time Complexity`*:<br>
O(h) where h is the height of the binary search tree. 
  
- *`Space Complexity`*:<br>
O(h) (worst case is O(n), best case is O(logn)
  

### My Solution 2：_`iteration`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        # UnboundLocalError：cur_node, parent_node = root, cur_node
        # 我们要用到current 遍历的前一个节点，所以要有两个variable
        cur_node, parent_node = root, root

        while cur_node:            
            parent_node = cur_node
            if cur_node.val > val:
                cur_node = cur_node.left           
            else:
                cur_node = cur_node.right

        # 确定是插入到 节点左边还是右边  
        if parent_node.val > val:
            parent_node.left = TreeNode(val)
        else:
            parent_node.right = TreeNode(val)
        
        return root
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(logn)for a balanced BST and O(n) for a skewed BST.
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "450"><a href="https://leetcode.com/problems/delete-node-in-a-bst">450. Delete Node in a BST</a></h2><h3>Medium</h3><p>Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return <em>the <strong>root node reference</strong> (possibly updated) of the BST</em>.</p>

<p>Basically, the deletion can be divided into two stages:</p>

<ol>
	<li>Search for a node to remove.</li>
	<li>If the node is found, delete the node.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg" style="width: 800px; height: 214px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 3
<strong>Output:</strong> [5,4,6,2,null,null,7]
<strong>Explanation:</strong> Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it&#39;s also accepted.
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg" style="width: 350px; height: 255px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 0
<strong>Output:</strong> [5,3,6,2,4,null,7]
<strong>Explanation:</strong> The tree does not contain a node with value = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [], key = 0
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>Each node has a <strong>unique</strong> value.</li>
	<li><code>root</code> is a valid binary search tree.</li>
	<li><code>-10<sup>5</sup> &lt;= key &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it with time complexity <code>O(height of tree)</code>?</p>




### My Solution 1：_`recursion with debug`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # first test failed so let's debug
        if not root:
            # print("root is None")
            return
        
        print(f"Current Node:{root.val}")
        
        if root.val == key:
            # print("key found")
            if not root.left and not root.right:
                return 
            
            elif root.left and not root.right:
                return root.left
            
            elif root.right and not root.left:
                return root.right
            
            else:
                cur_node = root.right
                # The issue happened at this statement-> cur_node
                while cur_node.left:
                    cur_node = cur_node.left
                # print(f"Minimum node in right subtree: {cur_node.val}")
                cur_node.left = root.left
                print(f"left subtree of root is {cur_node.left.val} ")
                print(f"right subtree of root is {root.right.val}")
                return root.right
        # process if key in left subtree
        if key < root.val:
            # print(f"Going left from {root.val }")
            root.left = self.deleteNode(root.left,key)
        # process if key in right subtree
        elif key > root.val:
            # print(f"Going right from {root.val}")
            root.right = self.deleteNode(root.right, key)
        
        # below part can be removed since the case root.val == key 
        # has been conisdered at the top 
        # else:
        #     print(f"Going root from here")
        #     return root
       
        return root
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
The overall time complexity is O(h), which would be O(log n) for a balanced BST and O(n) for a skewed BST

- *`Space Complexity`*:<br>
The space complexity is therefore O(h), which corresponds to O(log n) for a balanced BST and O(n) for a skewed BST due to the recursive function calls.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)

