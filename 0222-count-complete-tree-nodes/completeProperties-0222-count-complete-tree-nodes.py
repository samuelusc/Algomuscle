# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # implement the properties of complete binary tree
        #终止条件1
        if not root:
            return 0

        level = 1 #root is counted as 1
        left,right = root.left, root.right

        while left and right:
            level += 1
            left,right = left.left, right.right
        
        # 叶节点之后
        if not left and not right:
            # 节点数 = 2 ** level - 1 (1base)
            #终止条件2
            return 2 ** level - 1
        
        # post order traversal to count the numbers of nodes 
        # 单层递归逻辑
        leftNums = self.countNodes(root.left)
        rightNums = self.countNodes(root.right)
        result = leftNums + rightNums + 1
        return result

        # return self.countNodes(root.left) + self.countNodes(root.right) + 1
