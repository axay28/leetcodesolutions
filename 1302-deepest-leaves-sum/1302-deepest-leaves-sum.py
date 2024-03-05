# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        sum_=0
        while q:
            sum_=0
            for i in range(len(q)):
                popped=q.popleft()
                sum_+=popped.val
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                
        return sum_
        