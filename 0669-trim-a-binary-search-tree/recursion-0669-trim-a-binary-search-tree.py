# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        #base case
        if not root:
            return 
        #处理当前节点
        # 当前根节点<low, 去查看它的右子树找到符合 >= low 的并返回
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # 当前节点>hight, 去查看左子树 
        if root.val > high:
            return self.trimBST(root.left, low, high)


        # root.left 连接递归后的左节点
        root.left = self.trimBST(root.left, low, high)
        # root.right 连接递归后的右节点
        root.right = self.trimBST(root.right, low, high)
        #返回trimed root
        return root
