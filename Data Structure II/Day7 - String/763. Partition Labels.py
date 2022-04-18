class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance={val:i for i,val in enumerate(s)}
        output, ma, size=[],-1,1
        for i, val in enumerate(s):
            ma=max(ma,last_appearance[val])
            if i==ma:
                output.append(size)
                size=1
            else: size+=1
        return output