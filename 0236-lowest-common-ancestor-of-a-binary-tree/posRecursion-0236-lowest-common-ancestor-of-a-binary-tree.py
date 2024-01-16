# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # post-order -> left, right , root

        # base case: if current node is None,return None
        if not root:
            return None
        # base case: if current node matches either p or q,
        # return current node
        if root == p or root == q:
            return root

        # recursively search in the left / right subtree for p or q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # handling 4 cases based on the nodes
        # found in the left and right subtress

        # Case1:if left and right subtree are not None
        # means the current node is their lowest common ancestor
        if left and right:
            return root

        # Case 2: If both left and right are None,
        # it means neither p nor q are found in the subtree of the cur node
        if not left and not right:
            return None

        # Case3: either p or q found in the left subtree
        elif left:
            return left
        # Case4: either p or q found in the right subtree
        else:
            return right
