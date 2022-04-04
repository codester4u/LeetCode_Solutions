class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest=float("inf")
        index=-1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                if (abs(points[i][0]-x)+abs(points[i][1]-y))<smallest:
                    index=i
                    smallest=(abs(points[i][0]-x)+abs(points[i][1]-y))
                elif (abs(points[i][0]-x)+abs(points[i][1]-y))==smallest:
                    if i<index:
                        index=i
                        smallest=(abs(points[i][0]-x)+abs(points[i][1]-y))
        return index
                
        
        