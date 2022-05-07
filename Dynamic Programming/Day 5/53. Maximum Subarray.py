class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            if i>0 and dp[i-1]>0:
                dp[i] = dp[i-1] + num
            else:
                dp[i] = num
        return max(dp)