# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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