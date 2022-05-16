class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        cumsum = [[0]*n for _ in range(m)]

        cumsum[0][0] = mat[0][0]

        for row in range(1, m):
            cumsum[row][0] = cumsum[row-1][0] + mat[row][0]

        for col in range(1, n):
            cumsum_col = 0
            for row in range(m):
                cumsum[row][col] = cumsum[row][col-1] + cumsum_col + mat[row][col]
                cumsum_col += mat[row][col]


        res = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                start_row = row - k - 1
                start_col = col - k - 1

                end_row = min(row + k, m-1)
                end_col = min(col + k, n-1)

                if start_row < 0:
                    a = 0
                else:
                    a = cumsum[start_row][end_col]

                if start_col < 0:
                    b = 0
                else:
                    b = cumsum[end_row][start_col]

                if start_row < 0 or start_col < 0:
                    c = 0
                else:
                    c = cumsum[start_row][start_col]


                res[row][col] = cumsum[end_row][end_col] - a - b + c
        return res