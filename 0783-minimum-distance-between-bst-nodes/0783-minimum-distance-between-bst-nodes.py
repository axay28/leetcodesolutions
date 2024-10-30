# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        dfslist=[]
        def dfs(node):
            if node is None:
                return
            dfslist.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        dfslist.sort()
        mind=1e9
        for i in range(1,len(dfslist)):
            mind=min(mind,dfslist[i]-dfslist[i-1])
        return mind
        