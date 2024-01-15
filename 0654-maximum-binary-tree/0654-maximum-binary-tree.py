# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 构建树->前序遍历
        # base case,递归结束条件
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_value, index = 0, 0
        # 数组中找到root
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                index = i
        # 建立根
        node = TreeNode(max_value)
        
        #保证左子树至少有一个元素
        if index > 0:
            new_nums = nums[:index]
            #递归调用的结果来构建左子树
            node.left = self.constructMaximumBinaryTree(new_nums)
        
        # nums.size -1 保证至少右子树有一个元素
        if index < len(nums)-1:
            new_nums = nums[index+1:]
            node.right = self.constructMaximumBinaryTree(new_nums)
        
        # 返回根节点
        return node