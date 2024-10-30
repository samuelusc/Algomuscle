# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.findp = False
        self.findq = False
        res = self.find(root,p,q)
        if not self.findp or not self.findq:
            return None
        return res
    def find(self, root, p, q):
        if not root:
            return None
        
        left = self.find(root.left,p,q)
        right = self.find(root.right,p,q)

        if left and right:
            return root
        
        if root == p or root == q:
            if root == p:
                self.findp = True
            if root == q:
                self.findq = True
        
            return root

        return left if left else right
    