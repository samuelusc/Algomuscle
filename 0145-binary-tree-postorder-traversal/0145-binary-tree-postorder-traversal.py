# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []

        while stack:
            
            node = stack.pop()
            if node:
                res.append(node.val)
                # 注意这里和preOrder相反
                stack.append(node.left)
                stack.append(node.right)
        # 中，右，左，反转就是 左，中，右
        # return res[::-1]        
        res.reverse() # x.reverse()inplace modify and return None
        return res

