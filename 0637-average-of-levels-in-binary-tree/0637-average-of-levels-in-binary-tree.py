# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        if not root:
            return res
        
        queue = deque([root])

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            avg = sum(level) // len(level)
            res.append(avg)

        return res
