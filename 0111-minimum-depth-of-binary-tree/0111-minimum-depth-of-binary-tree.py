# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0
        
        dq = deque([root])
        mindepth = 0
        while dq:
            size = len(dq)
            mindepth += 1

            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

                if not node.left and not node.right:
                    return mindepth
        return mindepth