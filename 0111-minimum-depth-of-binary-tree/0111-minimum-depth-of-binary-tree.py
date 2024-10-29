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
        
        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        if leftHeight and not rightHeight:
            return 1 + leftHeight
        if not leftHeight and rightHeight:
            return 1 + rightHeight

        return 1 + min(leftHeight, rightHeight)