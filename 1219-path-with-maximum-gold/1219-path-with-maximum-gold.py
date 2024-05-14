class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(row,col):
            if row<0 or col<0 or row>=rows or col>=cols or grid[row][col]==0:
                return 0
            visited=grid[row][col]
            grid[row][col]=0
            
            maxgold=0
            maxgold=max(dfs(row+1,col),dfs(row,col+1),dfs(row-1,col),dfs(row,col-1))
            grid[row][col]=visited
            
            return visited+maxgold
        max_gold_collected = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] >= 0:
                    max_gold_collected = max(max_gold_collected, dfs(row, col))
        
        return max_gold_collected