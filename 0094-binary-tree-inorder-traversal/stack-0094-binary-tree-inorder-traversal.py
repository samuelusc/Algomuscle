# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [] # visited
        res =[]
        cur = root # current traversing 
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            
            else:
                # no left child
                cur = stack.pop()
                # push into final list 
                res.append(cur.val)
                #traverse right child of node
                cur = cur.right
        
        return res
                
        
