class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        for i in nums:
            tmp=[]
            for l in res:
                tmp.append(l+[i])
            res.extend(tmp)
        return [list(l) for l in set([tuple(l) for l in res])]