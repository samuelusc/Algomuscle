# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum depth encountered as negative infinity
        self.maxDepth = float('-inf')
        # Initialize the result to store the bottom-left value
        self.res = None

        # Start the traversal from the root node at depth 1
        self.traversal(root, 1)
        return self.res
    
    def traversal(self, node, depth):
        # If the node is a leaf node (no left and right children)
        if not node.left and not node.right:
            # Update the result if this leaf node is deeper than previously encountered ones
            if self.maxDepth < depth:
                self.maxDepth = depth
                self.res = node.val
            return 

        # Traverse the left subtree if it exists
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1  # Backtrack to previous depth after returning from recursion
        # Traverse the right subtree if it exists
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1  # Backtrack to previous depth after returning from recursion
        
        