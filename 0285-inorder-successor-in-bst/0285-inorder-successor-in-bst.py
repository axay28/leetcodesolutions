# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        #inorder - left node right
        if not root:
            return None
        elif p.val>=root.val:
            return self.inorderSuccessor(root.right,p)
        else:
            left= self.inorderSuccessor(root.left,p) # for p = 4 its successor is root
            return left if left else root
        
    