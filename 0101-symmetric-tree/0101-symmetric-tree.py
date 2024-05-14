# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return Tree

        
        stack = [root.left, root.right]
        while stack:
            nodeR = stack.pop()
            nodeL = stack.pop()

            if not nodeR and not nodeL:
                continue
            if not nodeR or not nodeL or nodeR.val != nodeL.val:
                return False

            stack.append(nodeL.left)
            stack.append(nodeR.right)
            stack.append(nodeL.right)
            stack.append(nodeR.left)
        
        return True