# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Initialize an empty list to store the final paths
        res = []
        # Initialize an empty list to store the current path
        path = []
        
        # if the root is None (empty tree)
        # return the empty result list
        if not root:
            return res

        # define a helper function to recursively find all paths
        def _getPaths(node, path, res):
            
            # Append the current Node's value to the path list
            path.append(str(node.val))
            # If the current node is a left node (no childre)
            # we will append the path to the result list
            if not node.left and not node.right:
                res.append('->'.join(path))
                return 
            # If the current node has a left child, recusively
            # find paths in the left subtree
            if node.left:
                _getPaths(node.left, path, res)

                # Backtrack by removing the last added node value from the path list
                path.pop()
            
            # If the current node has a right child, recusively 
            # find paths in the right subtree
            if node.right:
                _getPaths(node.right, path, res)

                # Backtrack by removing the last added node value from the path list 
                path.pop()

        # start the recursive function from the root node
        _getPaths(root, path, res)
        # return the final list of paths
        return res
