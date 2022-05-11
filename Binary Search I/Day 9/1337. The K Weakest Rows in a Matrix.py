class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic={}
        for i in range(len(mat)):
            dic[i]=sum(mat[i])
        l = sorted(dic.items(), key=lambda x:x[1])
        l=dict(l)
        x=list(l.keys())
        return x[:k]