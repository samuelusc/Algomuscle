# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        res = []
        if not root:
            return []
        
        dq = deque([root])
        
        while dq:
            largeNum = float('-inf')
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                largeNum = max(largeNum, node.val)
            
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            res.append(largeNum)
        return res