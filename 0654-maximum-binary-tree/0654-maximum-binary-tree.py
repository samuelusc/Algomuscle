# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 尽管 nums.size >= 1,但是递归后的数组有可能是空的
        # 检查nums是否为空
        if not nums:
            return None
        root = max(nums)
        index = nums.index(root)

        # 建立树的根节点
        node = TreeNode(root)    

        # 如果列表为空，递归会在 if not nums 时处理
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])

        return node