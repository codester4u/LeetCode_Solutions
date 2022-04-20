class Solution:
    def dfs(self, grid, r,c):
        grid[r][c]=0
        num=1
        lst=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for i, j in lst:
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j]==1:
                num+=self.dfs(grid,i,j)
        return num
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=max(area,self.dfs(grid,i,j))
        return area