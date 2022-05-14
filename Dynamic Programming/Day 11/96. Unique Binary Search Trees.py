class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        
        def helper(start, end):
            if start < 1 or end > n or start >= end:
                return 1
            count=0
            if(start, end) in memo:
                return memo[(start, end)]
            else:
                for i in range(start, end+1):
                    count+=(helper(start, i-1)*helper(i+1, end))
                memo[(start, end)]=count
                return count
        return helper(1,n )