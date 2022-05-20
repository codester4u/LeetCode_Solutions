class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        dp = [[0 for i in range(len(s)+1)] for i in range(len(s)+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1]==rev[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        return dp[len(s)][len(s)]