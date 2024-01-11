# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # implement stack to compute the number of nodes
        if not root:
            return 0
        
        res = 0
        stack = [root]
        
        while stack:
            level_size = len(stack)

            for _ in range(level_size):
                node = stack.pop()
                res += 1

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return res