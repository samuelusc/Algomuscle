# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dif = float('inf')
        self.pre_node = None
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.dif

    def inorder(self, cur_node):
        if not cur_node:
            return

        self.inorder(cur_node.left)

        if self.pre_node:
            self.dif = min(self.dif, cur_node.val - self.pre_node.val)
        
        self.pre_node = cur_node

        self.inorder(cur_node.right)