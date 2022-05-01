class Solution:
    def frequencySort(self, s: str) -> str:
        res=[]
        bucket=[[] for _ in range(len(s)+1)]
        
        for c, freq in Counter(s).items():
            bucket[freq].append(c)
            
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                res.append(j*i)
        return ''.join(res)
                