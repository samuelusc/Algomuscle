# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, right = root.left, root.right
        level = 1

        while left and right:
            left,right = left.left, right.right
            level += 1
        
        if not left and not right:
            return 2 ** level - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)