# Last updated: 14/6/2025, 2:41:54 pm
class Solution:
    def average(self, salary: List[int]) -> float:
        s = sum(salary)
        s -= min(salary)
        s -= max(salary)

        return s / (len(salary) - 2)