class Solution:
    def isValid(self, s: str) -> bool:
        op=[]
        close={')':'(',']':'[','}':'{'}
        for i in s:
            if i in close:
                if op and close[i]==op[-1]: op.pop()
                else: return False
            else: op.append(i)
        return True if not op else False
        