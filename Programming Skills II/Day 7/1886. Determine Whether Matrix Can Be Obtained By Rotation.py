class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rot(mat):
            mat.reverse()
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            return mat
        for i in range(4):
            mat=rot(mat)
            if mat==target: return True
        return False