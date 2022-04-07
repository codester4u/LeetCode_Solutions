class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res=[]
        for i in arr:
            res.append(bin(i)[2:].count('1'))
        ans=[]
        co=0
        while(co<=max(res)):
            x=[]
            for i in range(len(res)):
                #x=[]
                if res[i]==co:
                    x.append(arr[i])
                #print(x)
                x.sort()
            ans.extend(x)
            co+=1
        return ans
                    