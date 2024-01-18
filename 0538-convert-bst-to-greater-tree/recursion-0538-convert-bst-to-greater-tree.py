# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Two pointers 
        #inorder -> 到序遍历 右->中->左
       
        # previou val 设为0不改变最大值
        # 不设置pre_node 是避免None 情况
        self.pre_val = 0

        return self.traversal(root)
    

    def traversal(self, cur_node):
        if not cur_node:
            return 

        # right
        self.traversal(cur_node.right)

        # process root
        cur_node.val += self.pre_val
        self.pre_val = cur_node.val

        # left
        self.traversal(cur_node.left)
        
        return cur_node
