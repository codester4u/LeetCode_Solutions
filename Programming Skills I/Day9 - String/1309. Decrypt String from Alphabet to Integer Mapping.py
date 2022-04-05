class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic={str(i):chr(96+i) for i in range(1,27)}
        ans = ""
        dic['']=''
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                temp = ""
                for j in range(i - 2, i):
                    temp += s[j]
                ans = dic[str(temp)] + ans
                i -= 3
            else:
                ans = dic[str(s[i])] + ans
                i -= 1
        return ans
        