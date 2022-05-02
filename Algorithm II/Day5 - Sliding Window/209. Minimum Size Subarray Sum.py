class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("inf")
        su=0
        j=0
        
        for i, num in enumerate(nums):
            su+=num
            while su>=target:
                res=min(res, i-j+1)
                su-=nums[j]
                j+=1
        return res if res!=float("inf") else 0