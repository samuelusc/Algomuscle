# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def preOrder(node):
            # base case
            if not node:
                return 

            path.append(str(node.val))

            #如果到了叶节点
            if not node.left and not node.right:
                res.append('->'.join(path))

            else:
                preOrder(node.left)
                preOrder(node.right)

            path.pop()

        res = []
        path = []
        preOrder(root)
        return res

            
                
