"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        if not root:
            return None
        
        dq = deque([root])

        while dq:
            preNode = None
            size = len(dq)
            
            for _ in range(size):
                curNode = dq.popleft()
                if preNode:
                    preNode.next = curNode
                preNode = curNode

                if curNode.left:
                    dq.append(curNode.left)
                if curNode.right:
                    dq.append(curNode.right)
        
        return root