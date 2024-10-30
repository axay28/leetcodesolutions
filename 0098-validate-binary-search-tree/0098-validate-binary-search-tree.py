# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root:Optional[TreeNode], bottom = float('-inf'), top = float('inf'))-> bool:

        if root is None:
            return True
        return bottom < root.val < top and self.isValidBST(root.left, bottom, root.val) and self.isValidBST(root.right, root.val, top)
        