# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #后序遍历
        res = 0
        
        def postorder(cur_node):
            # Declare res as nonlocal to modify it within this function
            nonlocal res
            # base case
            if not cur_node: 
                return 2
            
            left = postorder(cur_node.left)
            right = postorder(cur_node.right)

            if left==2 and right == 2:
                return 0
            
            if left == 0 or right == 0:
                res += 1
                return 1
            
            if left == 1 or right == 1:
                return 2

        # 内部调用必须在定义后面
        # case 4 root is not covered
        if postorder(root) == 0:
            res += 1
        return res
        