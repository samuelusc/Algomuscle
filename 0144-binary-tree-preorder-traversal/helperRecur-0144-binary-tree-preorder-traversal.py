# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _helper(node):
            if not node:
                return

            res.append(node.val)
            _helper(node.left)
            _helper(node.right)
        
        _helper(root)
        return res
