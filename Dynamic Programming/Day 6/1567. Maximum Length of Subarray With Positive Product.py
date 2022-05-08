class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = pos = neg = 0
        for num in nums:
            if num > 0:
                pos=1+pos
                neg=1+neg if neg else 0
            elif num<0:
                pos, neg =1+neg if neg else 0, 1+pos
            else:
                pos = neg = 0
            res = max(res, pos)
        return res