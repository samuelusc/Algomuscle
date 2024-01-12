# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 前序遍历
        path = []
        result = []
        if not root:
            return result
        self.dfs(root, path, result)
        return result
    

    def dfs(self, cur_node, path, result):
        # 父节点 （中）
        path.append(cur_node.val)
        # 到达叶子节点
        if not cur_node.left and not cur_node.right:
            result.append('->'.join(map(str,path)))
            return 

        if cur_node.left:
            self.dfs(cur_node.left, path, result)
            path.pop()
        
        if cur_node.right:
            self.dfs(cur_node.right, path, result)
            path.pop()


    