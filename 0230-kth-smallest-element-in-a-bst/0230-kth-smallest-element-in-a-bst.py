# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.leftCount = 0

def nodeCount(node):
    if not node:
        return 0
    leftSize = nodeCount(node.left)
    rightSize = nodeCount(node.right)
    node.leftCount = leftSize
    return 1+ leftSize + rightSize
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeCount(root)
        cur = root
        while cur:
            if cur.leftCount + 1 == k:
                return cur.val
            
            elif cur.leftCount +1 < k:
                k -= cur.leftCount + 1
                cur = cur.right
            else:
                cur = cur.left
        
        return -1