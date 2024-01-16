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


