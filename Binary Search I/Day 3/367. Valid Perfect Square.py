class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l<r:
            m=(l+r)//2
            if m>=num/m:
                r=m
            else:
                l=m+1
        return l*l==num