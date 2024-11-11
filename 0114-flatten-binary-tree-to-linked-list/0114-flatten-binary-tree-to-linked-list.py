# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        leftSide = root.left
        rightSide = root.right

        root.left = None
        root.right = leftSide

        p = root
        while p.right is not None:
            p = p.right
        p.right = rightSide