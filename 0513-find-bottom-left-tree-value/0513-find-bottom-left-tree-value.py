# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Initialize a deque for level order traversal, starting with the root node
        queue = deque([root])

        # Variable to store the left-most value
        left_most = None

        # Perform level order traversal using the queue
        while queue:
            # Get the number of nodes at the current level
            size = len(queue)

            # Traverse all nodes at the current level
            for i in range(size):
                # Pop the node from the front of the queue
                node = queue.popleft()

                # Update left_most with the value of the first node at the current level
                if i == 0:
                    left_most = node.val

                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)

        # Return the left-most value at the bottom level
        return left_most