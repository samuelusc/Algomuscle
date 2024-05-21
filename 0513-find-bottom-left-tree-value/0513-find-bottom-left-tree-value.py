# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        left_most = None

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    left_most = node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return left_most