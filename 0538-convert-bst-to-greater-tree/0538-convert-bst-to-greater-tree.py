# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        def rightTraverse(node):
            if not node:
                return
            
            rightTraverse(node.right)
            node.val += self.pre
            self.pre = node.val
            rightTraverse(node.left)

        rightTraverse(root)
        return root