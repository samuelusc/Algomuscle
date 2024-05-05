# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
            else:
                node = stack.pop()
                res.append(node.val)

        return res