class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new=[]
        for i in matrix:
            new.extend(i)
        if target in new:
            return True
        return False
        