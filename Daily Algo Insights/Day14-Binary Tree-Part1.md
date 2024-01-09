# Day14 - Binary Tree Part 1


## Contents
* **[Introduction of Binary Tree](#Intro)**
* **[Binary Tree Traversal](#Traverse)**
* **[Recursion 101](#Recursion)**
* **[144.Binary Tree Preorder Traversal](#144)**
* **[145.Binary Tree Postorder Traversal](#145)**
* **[94.Binary Tree Inorder Traversal](#94)**


![Day14](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/day14.png)


<a name="Intro"></a>
## Binary Tree

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. Have a look at an elementary example of a binary tree:

![binary tree](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/day14-intro1.png)

## Depth of a Node

The length of the path from a node, n, to the root node. The depth of the root node is 0.

![Depth of Node](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/depth.gif)

## Height of a Tree 

The length of the path from n to its deepest descendant. The height of the tree itself is the height of the root node, and the height of leaf nodes is always 0.

![Depth of Node](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/height.gif)

## Full, Complete and Perfect Binary Trees

![Full,Complete, Perfect Binary Tree](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/full-complete-perfect.png)

### Full Binary Tree

Every node has 0 or 2 children.

### Complete Binary Tree

In a complete binary tree, every level except possibly the last, is completely filled and all nodes in the last level are as far left as possible.

### Perfect Binary Tree

All internals nodes have two children and all leaf nodes have the same level.


## Binary Search Tree

A binary search tree (BST) is a special type of binary tree, in which every nodes follows the ordering property of all left descendents < node < all right descendents.


<a name="Traverse"></a>
## Tree Traversal 

![Tree Traversal](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/traverse1.jpg)

### In-order Traversal: [A,B,C,D,E,F,G,H]

In-order traversal visits the left branch first, then the current node, and finally the right branch. The diagram below shows the traversal order of an in-order traversal on a binary tree.

### Pre-order Traversal: [F,B,A,D,C,E,G,H]

Pre-order traversal visits the current node first, then the left subtree, and finally the right subtree. The diagram below shows the traversal order of a pre-order traversal on a binary tree.

### Post-order Traversal [A,C,E,D,B,H,G,F]

Post-order traversal visits the left subtree first, then the right subtree, and finally the current node. The diagram below shows the traversal order of a post-order traversal on a binary tree.

<br>

## Recursion 101: The Three Ingredients You Need

![Recursion illustration](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day14/recursion.png
)


### A recursive algorithm must have a base case/exit.

A base case is the condition that allows the algorithm to stop recursing.

- A base case is typically a problem that is small enough to solve directly.

- In the factorial algorithm the base case is `n=1`.


### A recursive algorithm must change its state and move toward the base case.

We must arrange for a change of state that moves the algorithm toward the base case.

- A change of state means that some data that the algorithm is using is modified.

- Usually the data that represents our problem gets smaller in some way.

- In the factorial n decreases.

### A recursive algorithm must call itself, recursively.

Calling the function itself with different argument


## OR


### 确定递归函数的参数和返回值： 

- 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。

### 确定终止条件： 

- 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。

### 确定单层递归的逻辑： 

- 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。<br>



![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)

<h2 id = "144"><a href="https://leetcode.com/problems/binary-tree-preorder-traversal">144. Binary Tree Preorder Traversal</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary tree, return <em>the preorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 125px; height: 200px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>


### My Solution 1：_`Self-Recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        if not root:
            return res
        
        
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
        

```


### My Solution 2：_`Helper-Recursion`_  

  
```python

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _helper(node):
            if not node:
                return

            res.append(node.val)
            _helper(node.left)
            _helper(node.right)
        
        _helper(root)
        return res

```

### My Solution 3：_`Stack`_  

  
```python

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)

                # Stack is LIFO, 
                # Push right child first for Preorder
                stack.append(node.right)
                stack.append(node.left)
            

        return res
            
        

```


### My Solution 4：_`General-Stack`_  

  
```python

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                # stack 固定顺序先右后左
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)
                # preorder 最后放根结点
                stack.append(node)
                stack.append(None)
            
            else:
                node = stack.pop()
                res.append(node.val)
        
        return res
            
        

```

**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
<br>

![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)

<h2 id = "145"><a href="https://leetcode.com/problems/binary-tree-postorder-traversal">145. Binary Tree Postorder Traversal</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a&nbsp;binary tree, return <em>the postorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg" style="width: 127px; height: 200px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?


### My Solution 1：_`Self-Recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res
        
        

```


### My Solution 2：_`Helper-Recursion`_  

  
```python

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def _postOrder(node):
            if not node:
                return

            _postOrder(node.left)
            _postOrder(node.right)
            res.append(node.val)
        
        _postOrder(root)
        return res

```

### My Solution 3：_`Stack`_  

  
```python

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []

        while stack:
            
            node = stack.pop()
            if node:
                res.append(node.val)
                # 注意这里和preOrder相反
                stack.append(node.left)
                stack.append(node.right)
        # 中，右，左，反转就是 左，中，右
        # return res[::-1]        
        res.reverse() # x.reverse()inplace modify and return None
        return res
        

```


### My Solution 4：_`General-Stack`_  

  
```python

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #检查root,空返回[]
        if not root:
            return []
        #确保 root 非空将其设为stack的首个元素
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            # 如果没有遍历完左右子树
            if node:
                stack.append(node)
                # 空节点作为标记
                stack.append(None)
                # 依照Stack性质，right then left
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
            # node为None，到了叶节点
            else:
                # 弹出加入最终列表的节点
                node = stack.pop()
                res.append(node.val)
        
        return res
              
        

```

**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)
<br>

![dividing line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)


<h2 id = "94"><a href="https://leetcode.com/problems/binary-tree-inorder-traversal">94. Binary Tree Inorder Traversal</a></h2><h3>Easy</h3><p>Given the <code>root</code> of a binary tree, return <em>the inorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 125px; height: 200px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?


### My Solution 1：_`Self-Recursion`_  

  
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)

        return res
        
        

```


### My Solution 2：_`Helper-Recursion`_  

  
```python

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _inorder(node):
            if not node:
                return

            _inorder(node.left)
            res.append(node.val)
            _inorder(node.right)

        _inorder(root)
        return res

```

### My Solution 3：_`Stack`_  

  
```python

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [] # visited
        res =[]
        cur = root # current traversing 
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            
            else:
                # no left child
                cur = stack.pop()
                # push into final list 
                res.append(cur.val)
                #traverse right child of node
                cur = cur.right
        
        return res
                
        
        

```


### My Solution 4：_`General-Stack`_  

  
```python

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                # 中序遍历，push stack 顺序是右中左
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
                
            else:
                node = stack.pop()
                res.append(node.val)

        return res
              
        

```

**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(n)

