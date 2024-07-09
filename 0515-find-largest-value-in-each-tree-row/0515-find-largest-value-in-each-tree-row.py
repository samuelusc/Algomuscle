# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return res

        queue = deque([root])

        while queue:
            max_val = float("-inf")
            size = len(queue)


            for _ in range(size):
                 node = queue.popleft()
                 max_val = max(max_val, node.val)

                 if node.left:
                    queue.append(node.left)
                 if node.right:
                    queue.append(node.right)
            
            res.append(max_val)

        return res