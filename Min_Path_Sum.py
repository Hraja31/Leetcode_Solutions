class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
        
        for j in range(1,n):
            grid[0][j]+=grid[0][j-1]

        for x in range(1,m):
            for y in range(1,n):
                grid[x][y]+=min(grid[x-1][y],grid[x][y-1])
        
        return grid[-1][-1]
