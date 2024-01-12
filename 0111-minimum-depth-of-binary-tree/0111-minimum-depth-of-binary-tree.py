# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #通过高度计算深度
        #后续遍历-递归
        if not root:
            #查看例题root 深度1or0
            return 0 #root 深度1

        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        #区别于Max depth
        #判断是否一侧为空
        if not leftHeight and rightHeight:
            return 1 + rightHeight

        if not rightHeight and leftHeight:
            return 1 + leftHeight
        
        return 1 + min(leftHeight,rightHeight)