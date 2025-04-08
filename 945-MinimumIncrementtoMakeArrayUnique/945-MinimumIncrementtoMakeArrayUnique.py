# Last updated: 8/4/2025, 6:28:33 am
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        
        hash = defaultdict(int)
        mini = float('inf')
        maxi = 0

        for num in nums:
            mini = min(mini, num)
            maxi = max(maxi, num)
            hash[num] += 1
        
        res = 0
        for num in range(mini, maxi+1):
            if hash[num] > 1:
                hash[num+1] += hash[num]-1
                res += hash[num]-1

        res += hash[maxi+1] * (hash[maxi+1]-1) // 2
        return res

        

