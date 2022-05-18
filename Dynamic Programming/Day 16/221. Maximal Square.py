class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_edge = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    max_edge = max(max_edge, int(matrix[i][j]))
                elif matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i-1][j-1]), int(matrix[i][j-1]))+1
                    max_edge = max(max_edge, matrix[i][j])
        return max_edge**2