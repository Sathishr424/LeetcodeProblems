# Last updated: 12/6/2025, 5:45:26 am
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mini = float('inf')
        maxi = 0
        for num in nums:
            mini = min(num, mini)
            maxi = max(num, maxi)
        
        diff = maxi - mini
        return max(0, diff - (k*2))