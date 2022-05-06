class Solution:
    def jump(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[float('inf') for _ in range(N)]
        dp[0]=0
        i, jump, lastPos, maxPos=0, 0, 0, 0
        while i<N-1:
            maxPos=max(maxPos, i+nums[i])
            if i==lastPos:
                lastPos=maxPos
                jump+=1
            i+=1
        return jump