class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_index( nums, target, sign):
            left, right = 0 , len(nums)
            
            while left<right:
                mid=(left+right)//2
                if nums[mid]>target or (sign and target==nums[mid]):
                    right=mid
                else:
                    left=mid+1
            return left
        first_index= search_index(nums, target, True)
        
        if first_index == len(nums) or nums[first_index]!=target:
            return [-1,-1]
        last_index=search_index(nums, target, False)-1
        return [first_index, last_index]
