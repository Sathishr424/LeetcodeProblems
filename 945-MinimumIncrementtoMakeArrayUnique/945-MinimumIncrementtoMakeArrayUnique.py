# Last updated: 8/4/2025, 6:29:28 am
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        
        hash = defaultdict(int)
        mini = float('inf')
        maxi = 0

        for num in nums:
            mini = cmin(mini, num)
            maxi = cmax(maxi, num)
            hash[num] += 1
        
        res = 0
        for num in range(mini, maxi+1):
            if hash[num] > 1:
                hash[num+1] += hash[num]-1
                res += hash[num]-1

        res += hash[maxi+1] * (hash[maxi+1]-1) // 2
        return res

        

