# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth = float('-inf')
        self.res = None

        self.traversal(root, 1)
        return self.res
    
    def traversal(self, node, depth):
        
        if not node.left and not node.right:
            if self.maxDepth < depth:
                self.maxDepth = depth
                self.res =  node.val
            return 

        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
        
        