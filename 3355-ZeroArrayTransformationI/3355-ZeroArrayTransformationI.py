# Last updated: 20/5/2025, 1:38:44 pm
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        start = defaultdict(int)
        end = defaultdict(int)
        first = queries[0][0]
        last = queries[0][1]

        for x, y in queries:
            start[x] += 1
            end[y] += 1
        
        s = 0

        for i in range(n):
            s += start[i]

            nums[i] -= s
            if nums[i] > 0: return False

            s -= end[i]

        return True
            
        