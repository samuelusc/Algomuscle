# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        dq = deque([(root,1)])
        while dq:
            size = len(dq)

            for _ in range(size):
                node,depth = dq.popleft()
                if not node:
                    continue
                if not node.left and not node.right:
                    return depth
                if node.left:
                    dq.append((node.left, depth + 1))
                if node.right:
                    dq.append((node.right, depth +1)) 
        
            