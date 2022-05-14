class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        for i in range(2,rowIndex+2):
            tmp=[1]
            for j in range(1,i-1):
                tmp.append(res[-1][j-1]+res[-1][j])
            tmp.append(1)
            res.append(tmp)
        return res[-1]
        