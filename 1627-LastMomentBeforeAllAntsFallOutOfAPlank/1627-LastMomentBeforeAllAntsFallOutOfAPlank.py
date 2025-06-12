# Last updated: 12/6/2025, 5:41:12 am
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left) if left else 0, n - (min(right) if right else n))
