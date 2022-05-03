class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1]+[0 for _ in range(2,n+1)]
        for x in range(2,n+1):
            dp[x] = dp[x-1]+dp[x-2]
        return dp[n]