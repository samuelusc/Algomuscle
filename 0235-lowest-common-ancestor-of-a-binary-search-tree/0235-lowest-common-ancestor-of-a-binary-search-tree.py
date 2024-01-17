# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traversal(root, p, q)
    
    def traversal(self, cur_node, p, q):
        if not cur_node:
            return 
        
        if cur_node.val > p.val and cur_node.val > q.val:
            left = self.traversal(cur_node.left, p, q)
            if left: return left
        
        if cur_node.val < p.val and cur_node.val < q.val:
            right = self.traversal(cur_node.right, p, q)
            if right: return right
        
        return cur_node