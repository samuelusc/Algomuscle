# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        pre = 0
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            
            else:
                cur = stack.pop()
                cur.val += pre
                pre = cur.val
                cur = cur.left
        return root

        return root 