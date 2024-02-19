# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=None
        left=k

        def inorder(node):
            if not node:
                return
            nonlocal left
            inorder(node.left)
            left-=1
            nonlocal result
            if left==0:
                result= node.val
                return result
            inorder(node.right)
        inorder(root)
        return result