# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 高度： 后序遍历

        def postOrder(node):
            # base case
            if not node:
                return 0
            
            #单层递归逻辑，获取高度
            leftHeight = postOrder(node.left)
            rightHeight = postOrder(node.right)

            # 中层总结
            # 递归结束条件： 左右子树高度差1
            if leftHeight == - 1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1

            # 如果tree is balanced
            return 1 + max(leftHeight, rightHeight)

        # 空树也要考虑
        return postOrder(root) >= 0
