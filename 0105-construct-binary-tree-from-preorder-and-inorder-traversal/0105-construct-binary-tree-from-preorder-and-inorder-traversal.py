# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preStart, preEnd, inStart,inEnd):
            if preStart > preEnd:
                return None
            
            inVal = preorder[preStart]
            index = hashmap[inVal]

            leftSize = index - inStart

            node = TreeNode(inVal)
            node.left = build(preStart + 1, preStart + leftSize, inStart, index - 1)
            node.right = build(preStart + 1 + leftSize, preEnd, index+1, inEnd)

            return node
        
        hashmap = {val: i for i, val in enumerate(inorder)}
        return build(0,len(preorder)-1, 0, len(inorder)-1)