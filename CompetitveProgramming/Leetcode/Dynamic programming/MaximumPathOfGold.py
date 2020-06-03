class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m, res = len(grid), len(grid[0]), 0
        
        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            temp = grid[i][j]
            grid[i][j] = res = 0

            for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                if 0 <= x < n and 0 <= y < m:
                    res = max(res, dfs(x, y) + temp)
                    
            grid[i][j] = temp
            return res
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        
        return res