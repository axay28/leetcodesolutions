# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even=True
        q=deque([root])
        while q:
            prev=float("-inf") if even else float("inf")
            for _ in range(len(q)):
                popped=q.popleft()
                if even and (popped.val%2==0 or popped.val<=prev):
                    return False
                elif not even and (popped.val%2==1 or popped.val>=prev):
                    return False
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)    
                prev=popped.val
            even=not even
        return True