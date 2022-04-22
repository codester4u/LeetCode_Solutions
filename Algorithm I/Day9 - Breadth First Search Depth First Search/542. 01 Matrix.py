class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col=len(mat), len(mat[0])
        res=[]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    res.append((i,j))
                else:
                    mat[i][j]="."
        for i,j in res:
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r=i+x
                new_c=j+y
                if 0<=new_r<row and 0<=new_c<col and mat[new_r][new_c]==".":
                    mat[new_r][new_c]=mat[i][j]+1
                    res.append((new_r,new_c))
        return mat