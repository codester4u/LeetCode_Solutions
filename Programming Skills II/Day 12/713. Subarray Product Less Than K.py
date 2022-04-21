class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N=len(nums)
        prod, sub, total=1,0,0
        mini=0
        for i in range(N):
            prod*=nums[i]
            sub+=1
            
            while prod>=k and mini<=i:
                prod/=nums[mini]
                mini+=1
                sub-=1
            if prod<k:
                total+=sub
        return total
        