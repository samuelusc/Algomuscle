# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                #making a mistake at first by using queue.pop()
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_ave = sum(level) / level_size
            
            res.append(level_ave)
        
        return res


        
