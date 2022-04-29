class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res=[0] * n
        for a, b in trust:
            res[a-1]-=1
            res[b-1]+=1
        for i in range(n):
            if res[i]==n-1: return i+1
        return -1