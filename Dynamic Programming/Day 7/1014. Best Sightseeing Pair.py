class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res=0
        maxi=0
        for i in values:
            res=max(res, i+maxi)
            maxi=max(maxi, i)-1
        return res