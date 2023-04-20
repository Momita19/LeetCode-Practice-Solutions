class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        S = range(1,m)
        T = range(1,n)
        for i in T:
            grid[0][i] += grid[0][i-1]
        for j in S:
            grid[j][0] += grid[j-1][0]
        for i,j in product(S,T):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
        