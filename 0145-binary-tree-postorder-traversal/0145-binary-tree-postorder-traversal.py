# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #检查root,空返回[]
        if not root:
            return []
        #确保 root 非空将其设为stack的首个元素
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            # 如果没有遍历完左右子树
            if node:
                stack.append(node)
                # 空节点作为标记
                stack.append(None)
                # 依照Stack性质，right then left
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
            # node为None，到了叶节点
            else:
                # 弹出加入最终列表的节点
                node = stack.pop()
                res.append(node.val)
        
        return res
              
