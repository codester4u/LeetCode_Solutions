class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        su=[0 for i in range(len(nums))]
        su[0]=nums[0]
        for i in range(1,len(nums)):
            if su[i-1]<0:
                su[i]=nums[i]
            else:
                su[i]=su[i-1]+nums[i]
        return max(su)