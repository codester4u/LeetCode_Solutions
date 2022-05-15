class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N=len(triangle)
        cur, nex = triangle[N-2], triangle[N-1]
        
        for i in range(N-2,-1,-1):
            for j in range(i+1):
                cur[j]+=min(nex[j],nex[j+1])
            nex=cur
            cur=triangle[i-1]
        return nex[0]