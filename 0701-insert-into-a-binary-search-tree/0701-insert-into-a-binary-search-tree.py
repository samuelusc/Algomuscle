# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        # UnboundLocalError：cur_node, parent_node = root, cur_node
        # 我们要用到current 遍历的前一个节点，所以要有两个variable
        cur_node, parent_node = root, root

        while cur_node:            
            parent_node = cur_node
            if cur_node.val > val:
                cur_node = cur_node.left           
            else:
                cur_node = cur_node.right

        # 确定是插入到 节点左边还是右边  
        if parent_node.val > val:
            parent_node.left = TreeNode(val)
        else:
            parent_node.right = TreeNode(val)
        
        return root