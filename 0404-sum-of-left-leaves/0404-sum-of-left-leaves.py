# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #方法类似前序遍历    

        # 递归结束条件(base case)
        if not root:
            return 0
       
        #返回值初始化
        sum_left = 0
        
        # 先处理节点->类似前序的中
        # 单层递归逻辑：子叶就加到返回值中        
        if root.left and not root.left.left and not root.left.right:
            sum_left += root.left.val
        
        #递归函数的参数和返回值
        #前序的左右： 递归遍历左和右子树
        sum_left += self.sumOfLeftLeaves(root.left)
        sum_left += self.sumOfLeftLeaves(root.right)

        #最后返回
        return sum_left