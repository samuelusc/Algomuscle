# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 迭代 inorder
        stack =[]
        cur_node = root
        pre_node = None

        # 当两个中有一个为真
        while cur_node or stack:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            else:
                cur_node = stack.pop()
                if pre_node and cur_node.val <= pre_node.val:
                    return False

                pre_node = cur_node
                cur_node = cur_node.right
        
        return True

