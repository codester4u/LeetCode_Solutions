class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        x0 = arr[0][0]
        y0 = arr[0][1]
        x1 = arr[1][0]
        y1 = arr[1][1]
        dx = x1 - x0
        dy = y1 - y0
        for i in range(len(arr)):
            x = arr[i][0]
            y = arr[i][1]

            if (dx * (y - y1) != dy * (x - x1)):
                return False
        return True