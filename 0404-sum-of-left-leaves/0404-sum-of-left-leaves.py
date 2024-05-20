# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Initialize the result variable to store the sum of left leaves
        res = 0

        # If the root is None (empty tree), return the result (which is 0)
        if not root:
            return res

        # Initialize a stack with the root node for iterative traversal
        stack = [root]

        # Perform iterative traversal using the stack
        while stack:
            # Pop a node from the stack
            node = stack.pop()

            # Check if the left child exists and is a leaf node
            if node.left and not node.left.left and not node.left.right:
                # Add the value of the left leaf node to the result
                res += node.left.val

            # If the left child exists, push it onto the stack for further traversal
            if node.left:
                stack.append(node.left)
            
            # If the right child exists, push it onto the stack for further traversal
            if node.right:
                stack.append(node.right)

        # Return the final result which is the sum of all left leaf nodes
        return res

        