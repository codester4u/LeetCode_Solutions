class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        digitToLetters = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        res=[]
        def dfs(i, path):
            if i==len(digits):
                res.append(''.join(path))
                return
            for letter in digitToLetters[ord(digits[i])-ord('0')]:
                path.append(letter)
                dfs(i+1, path)
                path.pop()
        dfs(0,[])
        return res