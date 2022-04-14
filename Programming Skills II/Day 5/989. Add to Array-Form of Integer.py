class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num=''.join([str(i) for i in num])
        num=int(num)+k
        return [int(i) for i in str(num)]
        