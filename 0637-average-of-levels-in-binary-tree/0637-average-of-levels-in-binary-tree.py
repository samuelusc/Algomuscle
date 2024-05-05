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
            return 0
        
        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level = []
            count = 0

            for _ in range(size):
                node = queue.popleft()
                count += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ave = count / size
            res.append(ave)
        
        return res


        

