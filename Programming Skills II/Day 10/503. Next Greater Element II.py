class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        N=len(nums)
        lnums=nums*2
        
        for i in range(len(lnums)):
            while len(stack)>0 and stack[-1][0]<lnums[i]:
                val, pos=stack.pop()
                res[pos]=lnums[i]
            if i<N:
                stack.append((lnums[i],i))
        return res