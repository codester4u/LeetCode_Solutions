class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums)
        res=sorted(res,key=lambda x:res[x],reverse=True)
        
        return res[:k]