# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.robTree(root)
        return max(res[0],res[1])


    def robTree(self, cur_node):
        if not cur_node:
            return [0,0]

        leftDp = self.robTree(cur_node.left)
        rightDp = self.robTree(cur_node.right)

        val1 = cur_node.val + leftDp[0] + rightDp[0]
        val2 = max(leftDp[0],leftDp[1]) + max(rightDp[0],rightDp[1])

        return [val2,val1]    