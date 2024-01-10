# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # implement stack 
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            node_right = stack.pop()
            node_left = stack.pop()

            # 如果两个节点为空，继续循环查看stack其他节点
            if not node_left and not node_right:
                continue
            # 终止条件，任一为空或不等
            if not node_left or not node_right or node_left.val != node_right.val:
                return False
            #将子节点按对称顺序入栈
            stack.append(node_left.left)
            stack.append(node_right.right)
            stack.append(node_left.right)
            stack.append(node_right.left)
        #栈空并且没有非对称，返回True
        return True

