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

        queue = deque([root])
        res = []

        while queue:

            level = []
            queue_size = len(queue)

            for _ in range(queue_size):
                node = queue.popleft()
                level.append(node.val)

                # for child in (node.left,node.right):
                #     if child:
                #         queue.append(child)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            res.append(level)

        return res
                        


