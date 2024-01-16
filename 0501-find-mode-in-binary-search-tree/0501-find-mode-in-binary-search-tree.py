# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.count = 0
        self.max_count = 0
        self.pre_node = None

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder traversal

        # Base case: return if node is None
        if not root:
            return

        # Traverse the left subtree
        self.findMode(root.left)

        # Process the current node
        # Assign count as 1 if previous node is None
        if not self.pre_node:
            self.count = 1
        # Increment count if current node value equals previous node value
        elif self.pre_node.val == root.val:
            self.count += 1
        # Reset count to 1 if current node value is different
        else:
            self.count = 1

        # Update previous node to the current node
        self.pre_node = root

        # If count equals max_count, add current node value to res
        if self.count == self.max_count:
            self.res.append(root.val)
        # If count is greater than max_count, reset res and update max_count
        elif self.count > self.max_count:
            self.max_count = self.count
            self.res = [root.val]

        # Traverse the right subtree
        self.findMode(root.right)
        # Return the list of mode(s)
        return self.res
