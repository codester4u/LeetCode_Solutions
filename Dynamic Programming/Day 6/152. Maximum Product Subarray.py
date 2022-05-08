class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1: return 0
        res = cur_max = cur_min = nums[0]
        
        for i in nums[1:]:
            tmp = cur_max
            cur_max = max(cur_max*i, cur_min*i, i)
            cur_min = min(tmp*i, cur_min*i, i)
            res = max(res, cur_max)
        return res