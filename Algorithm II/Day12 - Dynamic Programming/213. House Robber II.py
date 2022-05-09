class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        dp1, dp2 = 0, 0
        for i in nums[:-1]:
            dp1, dp2 = max(dp2+i, dp1), dp1
        dpp1, dpp2 = 0, 0
        for i in nums[1:]:
            dpp1, dpp2 = max(dpp2+i, dpp1), dpp1
        return max(dp1, dpp1)