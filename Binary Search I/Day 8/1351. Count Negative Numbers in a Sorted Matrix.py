class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        
        i=0
        j=m-1
        res=0
        
        while i<n and j>=0:
            if grid[i][j]<0:
                res+=n-i
                j-=1
            else: i+=1
        return res