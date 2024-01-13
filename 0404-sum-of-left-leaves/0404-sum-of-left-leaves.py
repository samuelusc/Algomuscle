# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = self.traverse(root)
        if res != 0:
            return res
        else:
            return 0

    # 递归函数的参数和返回值
    def traverse(self, root):    
        #base case 递归终止条件 1
        if not root:
            return 0
        #递归终止条件 2 ->叶子节点
        if not root.left and not root.right:
            return 0
        
        #单层递归逻辑
        #先递归 -> 后检查是否叶节点
        leftNums = self.traverse(root.left)

        #回溯时再处理节点
        if root.left and not root.left.left and not root.left.right:
            leftNums = root.left.val
        
        #单层递归逻辑
        rightNums = self.traverse(root.right)

        res = leftNums + rightNums
        #递归返回值 ->int
        return res