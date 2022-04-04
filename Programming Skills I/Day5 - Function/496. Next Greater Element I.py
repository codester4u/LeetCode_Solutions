class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            for j in nums2[nums2.index(i)+1:]:
                if j>i:
                    res.append(j)
                    break
            else: res.append(-1)
        return res
        