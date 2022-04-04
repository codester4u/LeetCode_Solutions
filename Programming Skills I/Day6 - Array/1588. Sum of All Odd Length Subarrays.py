class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res=[]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if len(arr[i:j+1])%2!=0:
                    #print(arr[i:j+1])
                    res.append(sum(arr[i:j+1]))
        return sum(res)        