class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(2,numRows+1):
            tmp=[1]
            for c in range(1,i-1):
                tmp.append(res[-1][c-1]+res[-1][c])
            tmp.append(1)
            res.append(tmp)
        return res
            