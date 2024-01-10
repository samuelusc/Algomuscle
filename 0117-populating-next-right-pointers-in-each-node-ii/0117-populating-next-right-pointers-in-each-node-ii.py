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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])
        
        while queue:
            level = []
            level_size = len(queue)
            pre_node = None
            for _ in range(level_size):
                cur_node = queue.popleft()

                if pre_node:
                    pre_node.next = cur_node
                
                pre_node = cur_node 

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            cur_node.next = None
        
        return root