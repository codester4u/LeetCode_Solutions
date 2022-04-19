class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def helper(nums):
            if len(nums)<2: return False
            if len(nums)==2: return True
            nums.sort()
            d=nums[1]-nums[0]
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]!=d: return False
            return True
        res=[]
        for i in range(len(l)):
            res.append(helper(nums[l[i]:r[i]+1]))
        return res