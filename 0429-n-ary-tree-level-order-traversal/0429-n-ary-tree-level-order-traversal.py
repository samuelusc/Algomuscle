"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        dq = deque([root])

        while dq:
            level = []
            size = len(dq)
            
            for i in range(size):
                node = dq.popleft()
                level.append(node.val)

                for child in node.children:
                    if child:
                        dq.append(child)
            
            res.append(level)
        
        return res