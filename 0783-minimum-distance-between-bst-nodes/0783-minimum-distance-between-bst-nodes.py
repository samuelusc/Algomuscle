# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float('inf')
        self.pre_node = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        self.minDiffInBST(root.left)

        if self.pre_node:
            self.res = min(self.res, root.val - self.pre_node.val)
        
        self.pre_node = root
        
        self.minDiffInBST(root.right)

        return self.res