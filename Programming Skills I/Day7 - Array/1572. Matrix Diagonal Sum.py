class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1,d2=0,0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    d1+=mat[i][j]
                if i+j==len(mat)-1 and i!=j:
                    d2+=mat[i][j]
        return d1+d2
                
        