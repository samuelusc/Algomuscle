# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop()
                level.append(node.val)

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            res.append(level)
        return res