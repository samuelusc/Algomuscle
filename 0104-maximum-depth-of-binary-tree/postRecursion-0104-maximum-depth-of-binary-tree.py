# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #post-order traversal
        if not root:
            return 0

        # 计算左孩子
        leftHeight = self.maxDepth(root.left)

        #计算右孩子
        rightHeight = self.maxDepth(root.right)

        #返回给父节点
        # 1 是它本身 + 最大返回值
        result = 1 +  max(leftHeight, rightHeight)

        return result
