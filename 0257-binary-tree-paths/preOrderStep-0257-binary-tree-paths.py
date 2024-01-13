# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        if not root:
            return res
        self.preOrder(root, path, res)
        return res

    def preOrder(self, node, path, res):
        

        path.append(str(node.val))

        if not node.left and not node.right:
            res.append('->'.join(path))
            return
        
        if node.left:
            self.preOrder(node.left, path, res)
            path.pop()
        
        if node.right:
            self.preOrder(node.right, path, res)
            path.pop()
