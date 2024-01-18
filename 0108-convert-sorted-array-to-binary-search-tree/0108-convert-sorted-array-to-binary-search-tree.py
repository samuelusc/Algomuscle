# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.traversal(nums, 0, len(nums) -1)

    # 构造平衡二叉搜索树要从递增数组的中间选root
    # 递归构造 bst    
    def traversal(self, nums, left, right):
        if left > right:
            return

        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        root.left = self.traversal(nums, left, mid -1)
        root.right = self.traversal(nums, mid + 1, right)

        return root
    
