# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def _getHeight(node: Optional[TreeNode]) ->int:
            if not node:
                return 0

            leftH = _getHeight(node.left)
            if leftH == -1:
                return -1
            

            rightH = _getHeight(node.right)
            if rightH == -1:
                return -1
            

            if abs(leftH - rightH) > 1:
                return -1
            
            return 1 + max(leftH, rightH)
        
        height = _getHeight(root)
        return height != -1 