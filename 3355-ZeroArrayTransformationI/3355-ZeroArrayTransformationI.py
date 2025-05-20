# Last updated: 20/5/2025, 1:39:11 pm
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        line = [0] * (n+1)

        for x, y in queries:
            line[x] += 1
            line[y+1] -= 1
        
        s = 0
        zero = True
        for i in range(n):
            s += line[i]
            if nums[i] - s > 0: return False

        return True
            
        