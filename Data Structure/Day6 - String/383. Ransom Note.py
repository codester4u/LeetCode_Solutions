class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n,m=Counter(ransomNote),Counter(magazine)
        if n&m==n: return True
        return False
        