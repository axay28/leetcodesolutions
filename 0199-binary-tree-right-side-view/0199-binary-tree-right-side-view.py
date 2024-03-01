# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        if not root:
            return res
        q=deque([root])
        while q:
            res.append(q[0].val)
            for i in range(len(q)):
                popped=q.popleft()
                if popped.right:
                    q.append(popped.right)
                if popped.left:
                    q.append(popped.left)
        return res
                    