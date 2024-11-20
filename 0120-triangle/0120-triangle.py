class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(r,c):
            path=triangle[r][c]
            if r < len(triangle)-1:
                path+=min(dfs(r+1,c),dfs(r+1,c+1))
            return path
        return dfs(0,0)
