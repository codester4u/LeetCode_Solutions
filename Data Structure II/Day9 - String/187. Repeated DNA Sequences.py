class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N=len(s)
        coun=Counter([s[i-10:i] for i in range(10,N+1)])
        return [k for k,v in coun.items() if v>1]