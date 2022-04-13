class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep=''
        le=len(s)
        for i in range(le//2):
            rep+=s[i]
            if le%len(rep)==0:
                if rep*(le//len(rep))==s:
                    return True
        return False