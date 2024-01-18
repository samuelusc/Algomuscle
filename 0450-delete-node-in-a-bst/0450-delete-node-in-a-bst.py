# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # first test failed so let's debug
        if not root:
            print("root is None")
            return
        
        print(f"Current Node:{root.val}")
        
        if root.val == key:
            print("key found")
            if not root.left and not root.right:
                return 
            
            elif root.left and not root.right:
                return root.left
            
            elif root.right and not root.left:
                return root.right
            
            else:
                cur_node = root.right
                # The issue happened at this statement-> cur_node
                while cur_node.left:
                    cur_node = cur_node.left
                print(f"Minimum node in right subtree: {cur_node.val}")
                cur_node.left = root.left
                print(f"left subtree of root is {cur_node.left.val} ")
                print(f"right subtree of root is {root.right.val}")
                return root.right
        # process if key in left subtree
        if key < root.val:
            print(f"Going left from {root.val }")
            root.left = self.deleteNode(root.left,key)
        # process if key in right subtree
        elif key > root.val:
            print(f"Going right from {root.val}")
            root.right = self.deleteNode(root.right, key)
        
        # below part can be removed since the case root.val == key 
        # has been conisdered at the top 
        # else:
        #     print(f"Going root from here")
        #     return root
       
        return root