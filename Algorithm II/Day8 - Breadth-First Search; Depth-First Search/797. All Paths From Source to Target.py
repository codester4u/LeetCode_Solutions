class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        
        def dfs(u, path):
            if u==len(graph)-1:
                res.append(path)
                return 
            
            for v in graph[u]:
                dfs(v,path+[v])
                
        dfs(0,[0])
        return res