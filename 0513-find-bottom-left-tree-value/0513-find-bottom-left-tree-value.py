# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = float("-inf")
        self.res = None
        self.traversal(root, 0)
        return self.res

    def traversal(self, root, depth):
        if not root.left and not root.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = root.val
            
        if root.left:
            self.traversal(root.left, depth + 1)

        if root.right:
            self.traversal(root.right, depth + 1)
