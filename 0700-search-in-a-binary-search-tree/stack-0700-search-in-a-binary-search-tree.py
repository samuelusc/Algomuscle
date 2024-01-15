# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 使用单独变量，不会改变原始树的结构root 指针
        cur = root

        while cur:
            if cur.val > val:
                cur = cur.left
            
            elif cur.val < val:
                cur = cur.right
            
            else:
                return cur
        #没找到返回None
        return None
