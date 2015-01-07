class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    #dp
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = [[0 for i in range(n)] for i in range(m)]
        res[0][0] = grid[0][0]
        for i in range(1,m):
            res[i][0] = grid[i][0]+res[i-1][0]
        for i in range(1,n):
            res[0][i] = grid[0][i]+res[0][i-1]
            
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = min(res[i-1][j],res[i][j-1]) + grid[i][j]
        return res[m-1][n-1]
         
