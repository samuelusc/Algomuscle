# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        getLeft = self.minDepth(root.left)
        getRight = self.minDepth(root.right)

        if root.left and not root.right:
            return 1 + getLeft
        
        if not root.left and root.right:
            return 1 + getRight
        
        return 1 + min(getLeft, getRight)
