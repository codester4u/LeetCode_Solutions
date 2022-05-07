class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalsum, currmaxsum, currminsum =0, 0, 0
        maxsum=float("-inf")
        minsum=float("inf")
        
        for i in nums:
            totalsum+=i
            currmaxsum=max(currmaxsum+i, i)
            currminsum=min(currminsum+i, i)
            maxsum=max(maxsum, currmaxsum)
            minsum=min(minsum, currminsum)
            
        return maxsum if maxsum<0 else max(maxsum, totalsum-minsum)