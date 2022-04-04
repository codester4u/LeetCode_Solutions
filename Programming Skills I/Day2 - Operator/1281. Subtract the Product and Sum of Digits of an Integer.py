class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        su=0
        for i in str(n):
            prod*=int(i)
            su+=int(i)
        return prod-su
        