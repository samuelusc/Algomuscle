# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Define a helper function to calculate the height of the tree
        def _getHeight(node):
            # If the node is None, the height is 0
            if not node:
                return 0
            # Recursively calculate the height of the left subtree
            left_tree = _getHeight(node.left)
            if left_tree == -1:
                return -1

            # Recursively calculate the height of the right subtree
            right_tree = _getHeight(node.right)
            # If the right subtree is unbalanced, return -1
            if right_tree == -1:
                return -1

            # if the diff between left and right sbutrees is greater than 1
            # return -1 indicating unbalanced
            if abs(left_tree - right_tree) > 1:
                return -1
            # return the height of the current node
            return 1 + max(left_tree, right_tree)

        # call the helper function to check the root node
        res = _getHeight(root)
        # If the result is not -1, the tree is balanced, return True
        # Otherwise return False
        return res != -1
