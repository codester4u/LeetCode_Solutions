class Solution:
    def average(self, salary: List[int]) -> float:
        Total=sum(salary)-min(salary)-max(salary)
        return Total/(len(salary)-2)
        