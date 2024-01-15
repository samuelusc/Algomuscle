# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not neccesary the left child,but the leftmost value in the bottom
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #initialzie the result and minDepth
        # 设为实例属性
        self.result = 0
        self.minDepth = float("-inf")

        return self.traversal(root, 0)


    def traversal(self, node, depth):
        # Base case: if the node is a leaf node
        if not node.left and not node.right:
            # Update the result and minDepth
            if depth > self.minDepth:
                self.minDepth = depth
                self.result = node.val
        #If the node has a left child traversae left subtree
        # 先左后右   
        if node.left:
            depth += 1
            self.traversal(node.left,depth)
            #backtracking step , decrement depth
            depth -= 1

        #If the node has a right child    
        if node.right:
            depth += 1
            self.traversal(node.right,depth)
            depth -= 1
        
        return self.result
