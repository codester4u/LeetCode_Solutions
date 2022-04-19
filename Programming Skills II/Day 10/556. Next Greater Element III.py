class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=list(map(int,str(n)))
        
        i=len(n)-2
        while i>=0 and n[i]>=n[i+1]:
            i-=1
        if i==-1: return -1
        
        j=len(n)-1
        while n[j]<=n[i]:
            j-=1
            
        n[i],n[j]=n[j],n[i]
        n[i+1:]=reversed(n[i+1:])
        
        res=""
        for i in n:
            res+=str(i)
        res=int(res)
        
        return res if res<=2**31-1 else -1