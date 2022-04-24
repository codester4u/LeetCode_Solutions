class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[""]
        
        for i in s:
            tmp=[]
            if i.isalpha():
                for j in res:
                    tmp.append(j+i.lower())
                    tmp.append(j+i.upper())
            else:
                for j in res:
                    tmp.append(j+i)
            res = tmp
        return res