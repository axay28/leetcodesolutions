# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=0
        left=k
        def dfs(node):
            if not node:
                return 
            nonlocal left
            dfs(node.left)
            left-=1
            nonlocal result
            if left==0:
                result=node.val
                return result
            dfs(node.right)
        dfs(root)
        return result
        