# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Post-Order traversal

        # 结束条件
        if not root:
            return 0
        #左子树
        left_count = self.countNodes(root.left)
        #右子树
        right_count = self.countNodes(root.right)
        #中节点
        result = left_count + right_count + 1

        return result
