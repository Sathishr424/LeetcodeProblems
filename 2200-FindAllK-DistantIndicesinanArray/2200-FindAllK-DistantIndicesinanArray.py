# Last updated: 24/6/2025, 2:15:14 pm
inf = 10 ** 20
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ret = []
        
        nearest = [0] * n

        prev = inf
        for i in range(n):
            if nums[i] == key:
                prev = i
            nearest[i] = abs(i - prev)
        
        prev = inf
        for i in range(n-1, -1, -1):
            if nums[i] == key:
                prev = i
            nearest[i] = min(nearest[i], abs(prev - i))
        
        for i in range(n):
            if nearest[i] <= k:
                ret.append(i)
        
        return ret
