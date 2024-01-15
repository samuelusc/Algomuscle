# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如过树为空，或树的根节点就是 target value
        if not root or root.val == val:
            return root
        #initialize res to None
        res = None

        # 当根节点value > target value时
        if root.val > val:
            #将查找结果存入res
            res = self.searchBST(root.left, val)

        else:
            res = self.searchBST(root.right, val)

        return res