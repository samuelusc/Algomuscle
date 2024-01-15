# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Constrain 保证至少有一个node
        # 注意！ 层级遍历要用queue 而不是 stack     
        queue = deque([root])
    
        while queue:
            level_size = len(queue)

            # 取每行第一个node.val
            for i in range(level_size):
                node = queue.popleft()

                # 将第一个node.val 赋给 left_most
                if i == 0:
                    leftmost = node.val
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost