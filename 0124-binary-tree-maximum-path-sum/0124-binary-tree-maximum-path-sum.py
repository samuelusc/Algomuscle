# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def _oneSideMax(node):
            if not node:
                return 0
            
            leftMax = max(0, _oneSideMax(node.left))
            rightMax = max(0, _oneSideMax(node.right))

            nonlocal maxSum
            maxSum = max(maxSum, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        maxSum = float('-inf')
        _oneSideMax(root)
        return maxSum