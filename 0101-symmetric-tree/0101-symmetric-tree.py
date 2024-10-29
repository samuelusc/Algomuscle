# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        dq = deque([root.left, root.right])

        while dq:
            node1 = dq.popleft()
            node2 = dq.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            dq.append(node1.left)
            dq.append(node2.right)
            dq.append(node1.right)
            dq.append(node2.left)
        
        return True