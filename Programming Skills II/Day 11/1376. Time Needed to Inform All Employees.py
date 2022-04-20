import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_employee=collections.defaultdict(list)
        for i,j in enumerate(manager):
            if i!=-1:
                manager_employee[j].append(i)
        res=0
        def dfs(node,time):
            nonlocal res
            res=max(res,time)
            for i in manager_employee[node]:
                dfs(i, time+informTime[i])
        dfs(headID, informTime[headID])
        return res