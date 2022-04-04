class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        x=min(len(word1),len(word2))
        for i in range(x):
            res+=word1[i]
            res+=word2[i]
        if len(word1)>len(word2): y=word1[x:]
        else: y=word2[i+1:]
        return res+y