"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        que = deque([root])

        while que:
            size = len(que)
            pre = None

            for _ in range(size):
                cur = que.popleft()

                if pre:
                    pre.next = cur
                
                pre = cur
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            cur.next = None
        return root