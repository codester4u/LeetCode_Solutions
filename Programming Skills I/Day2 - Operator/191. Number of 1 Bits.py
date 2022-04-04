class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while(True):
            if n==0: break
            if n&1==1: cnt+=1
            n=n//2
        return cnt
        