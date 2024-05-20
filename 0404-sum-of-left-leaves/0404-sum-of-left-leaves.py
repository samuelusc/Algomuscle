# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Call the helper function postOrder to compute the sum of left leaves
        res = self.postOrder(root)
        # Return the result
        return res
    
    def postOrder(self, node):
        # If the current node is None, return 0
        if not node:
            return 0

        # If the current node is a leaf node, return 0
        if not node.left and not node.right:
            return 0

        # Recursively calculate the sum of left leaves in the left subtree
        leftNums = self.postOrder(node.left)
        
        # If the left child exists and is a leaf node, add its value to leftNums
        if node.left and not node.left.left and not node.left.right:
            leftNums = node.left.val
        
        # Recursively calculate the sum of left leaves in the right subtree
        rightNums = self.postOrder(node.right)
    
        # Return the sum of leftNums and rightNums
        return leftNums + rightNums
    