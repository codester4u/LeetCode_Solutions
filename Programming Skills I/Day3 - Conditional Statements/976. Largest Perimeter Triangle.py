class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            #print(nums[i:i+3])
            a,b,c=nums[i],nums[i+1],nums[i+2]
            #print(a,b,c)
            if(a+b>c and b+c>a and c+a>b):
                res.append(a+b+c)
        if len(res)>0: return max(res)
        return 0
        