# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 采用后序遍历：需要收集孩子信息然后向上层返回的这类题目
        # left,right then root

        def is_mirror(node1: TreeNode, node2: TreeNode):
            
            if not node1 and not node2:
                return True
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

        # empty tree is symmetric
        if not root:
            return True
        
        # slice tree into left subtree adn right subtree
        return is_mirror(root.left, root.right)
