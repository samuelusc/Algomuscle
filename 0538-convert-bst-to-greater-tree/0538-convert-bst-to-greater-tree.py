# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stack 模版-> 右中左 
        stack = []
        pre_val = 0
        cur_node = root

        while stack or cur_node:
            if cur_node:
                stack.append(cur_node)
                #遍历右
                cur_node = cur_node.right

            else:
                # 中处理
                cur_node = stack.pop()
                cur_node.val += pre_val
                pre_val = cur_node.val
                # 遍历左
                cur_node = cur_node.left
        
        return root

