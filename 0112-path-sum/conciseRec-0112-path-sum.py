# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sumNode):
            if not root:
                return False
            
            sumNode += root.val

            if not root.left and not root.right and sumNode == targetSum:
                return True

            return dfs(root.left, sumNode) or dfs(root.right, sumNode)
        
        return dfs(root, 0)
