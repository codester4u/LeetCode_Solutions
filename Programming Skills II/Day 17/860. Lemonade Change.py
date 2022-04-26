class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n5 = 0
        n10 = 0
        n20 = 0
        for i in bills:
            if i == 5:
                n5 += 1
            elif i == 10:
                n10 += 1
            else:
                n20 += 1
            if len(bills) > 0 and n5 == 0:
                return(False)
            if i == 20 and n10 > 0 and n5 > 0:
                n10 -= 1
                n5 -= 1
            elif i == 20 and n10 == 0 and n5 < 3:
                return(False)
            elif i == 20 and n10 == 0 and n5 >= 3:
                n5 = n5 -3
            if i == 10 and n5 > 0:
                n5 -= 1
            elif i == 10 and n5 == 0:
                return (False)
        return(True)
            