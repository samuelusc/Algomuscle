# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #设置类的成员变量防止递归重置
    def __init__(self):
        self.pre_val = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 中序遍历
        # 如果空树，则返回True
        if not root:
            return True
        
        #下面是出错的语句，递归每次都重置pre_val
        # pre_val = float('-inf')
        
        
        #遍历左子树
        left_valid = self.isValidBST(root.left)

        #遍历的中节点永远大于前一个节点
        if root.val > self.pre_val:
            self.pre_val = root.val
        #否则返回False
        else:
            return False
        # 遍历右子树
        right_valid = self.isValidBST(root.right)
        #返回左右子树的判断
        return left_valid and right_valid