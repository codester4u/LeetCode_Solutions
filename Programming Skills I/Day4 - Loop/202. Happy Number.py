class Solution:
    def isHappy(self, n: int) -> bool:
        se=set()
        flag=True
        while(flag):
            su=0
            for i in str(n):
                su+=(int(i)**2)
            n=su
            if su==1: return True
            else:
                if su not in se:
                    se.add(su)
                else: return False