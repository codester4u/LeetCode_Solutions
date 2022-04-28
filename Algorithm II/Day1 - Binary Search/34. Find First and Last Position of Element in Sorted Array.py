class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if nums[i]==target: res.append(i)
        #print(res)
        if len(res)>=1 :return [min(res),max(res)]
        return [-1,-1]
        