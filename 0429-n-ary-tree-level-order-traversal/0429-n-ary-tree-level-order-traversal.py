"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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

                for child in node.children:
                    queue.append(child)

            res.append(level)
        
        return res
                