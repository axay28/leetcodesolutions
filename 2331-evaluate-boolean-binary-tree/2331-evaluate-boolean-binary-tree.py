# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val!=0
        left_=self.evaluateTree(root.left)
        right_=self.evaluateTree(root.right)
        if root.val==2:
            root_=left_ or right_
        else:
            root_=left_ and right_
        return root_