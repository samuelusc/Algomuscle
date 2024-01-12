# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) != -1:
            return True
        else:
            return False


    def getHeight(self, root:TreeNode) -> int:
        # base case 递归结束条件
        if not root:
            return 0

        # 单层递归逻辑
        # 左子树不平衡 = -1
        leftHeight = self.getHeight(root.left) 
        if leftHeight == -1:
            return -1
        
        # 右子树不平衡 = -1
        rightHeight = self.getHeight(root.right) 
        if rightHeight == -1:
            return -1
        
        # 父节点汇总 （中）
        if abs(leftHeight - rightHeight) > 1:
            return -1 
        else:
            return 1 + max(leftHeight, rightHeight)
    
        

        