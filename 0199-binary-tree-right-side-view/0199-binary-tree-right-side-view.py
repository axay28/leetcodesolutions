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
            rightside=None
            for i in range(len(q)):
                popped=q.popleft()
                if popped:
                    rightside=popped
                    q.append(popped.left)
                    q.append(popped.right)
            if rightside:
                res.append(rightside.val)
        return res
                    