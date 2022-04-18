class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        seen={}
        for i in range(len(pattern)):
            if pattern[i] in seen:
                if s[i]!=seen[pattern[i]]:
                    return False
            else:
                if s[i] in list(seen.values()):
                    return False
                else:
                    seen[pattern[i]]=s[i]
        #print(seen)
        return True