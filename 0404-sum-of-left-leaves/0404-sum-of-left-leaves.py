# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        return self.postOrder(root)

    
    def postOrder(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 0
        
        leftNums = self.postOrder(node.left)

        if node.left and not node.left.left and not node.left.right:
            leftNums = node.left.val
        
        rightNums = self.postOrder(node.right)

        return leftNums + rightNums
