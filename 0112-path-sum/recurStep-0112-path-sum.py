# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # self.traversal(root, target) is incorrect such as
        # ([1],1)
        return self.traversal(root, targetSum - root.val)

    def traversal(self, root, count):
        if not root.left and not root.right:
            return count == 0

        if root.left:
            count -= root.left.val
            if self.traversal(root.left, count):
                return True
            count += root.left.val

        if root.right:
            count -= root.right.val
            if self.traversal(root.right, count):
                return True
            count += root.right.val

        return False
        


        
