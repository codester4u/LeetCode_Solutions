class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        A=self.nums.copy()
        for i in range(len(A)-1, 0, -1):
            j = randint(0,i)
            A[i], A[j] = A[j], A[i]
        return A


