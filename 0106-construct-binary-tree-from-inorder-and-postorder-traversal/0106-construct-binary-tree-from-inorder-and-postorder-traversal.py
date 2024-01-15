# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(val=root_val)

        index = inorder.index(root_val)
        # 中序遍历的根节点index也是后序遍历左右结点的分界
        root.left = self.buildTree(inorder[:index],postorder[:index])
        
        root.right = self.buildTree(inorder[index + 1:],postorder[index: -1])
        return root