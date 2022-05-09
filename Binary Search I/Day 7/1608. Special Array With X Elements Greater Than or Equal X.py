class Solution:
    def specialArray(self, nums: List[int]) -> int:
        comp=[0]*1001
        for num in nums:
            comp[num]+=1
        N=len(nums)
        for i in range(1001):
            if i == N:
                return i
            N-=comp[i]
        return -1
            
        
        
        