class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.dp=[[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                self.dp[i][j]=matrix[i-1][j-1]+self.dp[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output=0
        for i in range(row1+1,row2+2):
            output+=self.dp[i][col2+1]-self.dp[i][col1]
        return output


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)