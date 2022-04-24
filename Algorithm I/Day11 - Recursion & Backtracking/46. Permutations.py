class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        if len(nums)==1: return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            per=self.permute(nums)
            
            for perm in per:
                perm.append(n)
            res.extend(per)
            nums.append(n)
        return res