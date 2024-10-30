# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        hashset = set()
        for node in nodes:
            hashset.add(node.val)
        return self.find(root, hashset)
    
    def find(self, root, hashset):
        if not root:
            return None
        if root.val in hashset:
            return root
        
        left = self.find(root.left, hashset)
        right = self.find(root.right, hashset)

        if left and right:
            return root
        
        return left if left else right