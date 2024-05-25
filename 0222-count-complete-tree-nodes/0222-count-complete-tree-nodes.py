# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if not root:
            return 0

        countNum = 1  # Initialize the counter to 1 to include the root node

        left, right = (
            root.left,
            root.right,
        )  # Initialize pointers for left and right subtrees

        # Traverse the left and right subtree heights
        while left and right:
            countNum += 1  # Increment the counter for each level
            left, right = (
                left.left,
                right.right,
            )  # Move to the next level of left and right subtrees

        # If left and right both reach leaf nodes, it's a full binary tree
        if not left and not right:
            return 2**countNum - 1  # Full binary tree node count formula: 2^h - 1

        # If it's not a full binary tree, recursively count nodes in left and right subtrees and add 1 for the root
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
