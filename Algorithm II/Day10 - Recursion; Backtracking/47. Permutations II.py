class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        count={n:0 for n in nums}
        for i in nums:
            count[i]+=1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            for i in count:
                if count[i]>0:
                    perm.append(i)
                    count[i]-=1
                    
                    dfs()
                    
                    count[i]+=1
                    perm.pop()
        dfs()
        return res