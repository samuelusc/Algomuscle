# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    SEP = ","
    NULL = "#"
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        treeList = []
        self._serialize(root, treeList)
        return "".join(treeList)

    def _serialize(self, root, treeList):
        if not root:
            treeList.append(self.NULL)
            treeList.append(self.SEP)
            return None
        
        treeList.append(str(root.val))
        treeList.append(self.SEP)

        self._serialize(root.left,treeList)
        self._serialize(root.right,treeList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(self.SEP))
        return self._deserialize(nodes)
    def _deserialize(self,nodes):
        if not nodes:
            return None
        
        start = nodes.popleft()
        if start == self.NULL:
            return None
        root = TreeNode(int(start))
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))