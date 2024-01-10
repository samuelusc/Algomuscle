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
        # Option[x] 相当于 Union[x, None]参数为x或None
        # Union from typing module ：指定一个变量可以为几种类型中任意一种
        # Union[str, int] 表该参数可以为str or int
        if not root:
            return None

        queue = deque([root])

        while queue:
            pre_node = None
            level_size = len(queue)

            for _ in range(level_size):
                cur_node = queue.popleft()

                if pre_node:
                    pre_node.next = cur_node
                pre_node = cur_node

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            #最后一个节点设置的下一节点设置为None
            #cur_node在for外仍指向对列最后一个元素
            cur_node.next = None
        
        return root
            
                
        
