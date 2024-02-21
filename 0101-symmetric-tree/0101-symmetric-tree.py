# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        return self.issame(root.left,root.right)
        
    def issame(self,root_left,root_right):
        if root_left == None and root_right == None:
            return True
        if root_left==None or root_right ==None:
            return False
        if root_left.val!=root_right.val:
            return False
        return self.issame(root_left.left, root_right.right) and self.issame(root_left.right, root_right.left)

        
        