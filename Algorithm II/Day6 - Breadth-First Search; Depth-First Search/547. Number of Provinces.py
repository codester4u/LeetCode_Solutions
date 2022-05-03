class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res=0
        visited=set()
        def dfs(neighbours):
            for i,j in enumerate(neighbours):
                if j and i not in visited:
                    visited.add(i)
                    dfs(isConnected[i])
        for city, neighbours in enumerate(isConnected):
            if city not in visited:
                res+=1
                dfs(neighbours)
        return res
