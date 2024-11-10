# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node):
            if not node:
                return "#"
            
            left = serialize(node.left)
            right = serialize(node.right)

            subTree = left + "," + right + "," + str(node.val)

            fre = hashmap.get(subTree, 0) + 1
            hashmap[subTree] = fre
            if fre == 2:
                res.append(node)
            
            return subTree
        
        hashmap = {}
        res = []
        serialize(root)
        return res