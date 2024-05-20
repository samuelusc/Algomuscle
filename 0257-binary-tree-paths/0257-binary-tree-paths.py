# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # define a internal function to recursively find all paths
        # from root to leaf nodes
        def _findPaths(node, path, res):
            # If the current node is None, return None
            if not node:
                return
            # Append the current node's value to the path list            
            path.append(str(node.val))
            # If the current node is a leaf node (no children), append the path to the result list
            if not node.left and not node.right:
                res.append('->'.join(path))
                                   
            else:
                # Recursively find paths in the left subtree 
                _findPaths(node.left, path, res)
                # Recursively find paths in the right subtree 
                _findPaths(node.right, path, res)
            # Backtrack by removing the last added node value from the path list            
            path.pop()
        
        # Initialize an empty list to store the final paths
        res = []
        # Initialize an empty list to store the current path
        path = []
        # Start the recursive function from the root node
        _findPaths(root, path, res)
        # Return the final list of paths
        return res