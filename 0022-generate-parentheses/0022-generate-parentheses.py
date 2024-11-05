class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(start='', left=0, right=0):
            if len(start) == 2 * n:
                res.append(start)
                return
            if left < n:
                backtrack(start + '(', left + 1, right)
            if right < left:
                backtrack(start + ')', left, right + 1)

        res = []
        backtrack()
        return res
