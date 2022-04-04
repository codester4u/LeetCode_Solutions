class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1,c2=[],[]
        for i in range(len(s2)):
            if s1[i]!=s2[i]:
                c1.append(s1[i])
                c2.append(s2[i])
        if len(c1)==len(c2)==0:
            return True
        if len(c1)==len(c2)==2:
            if c1[0]==c2[1] and c1[1]==c2[0]:
                return True
        return False
            
        