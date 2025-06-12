# Last updated: 12/6/2025, 5:34:16 am
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        ret = 0
        for num in nums:
            hash[num] += 1
            
        ret = -float('inf')
        curr = 0
        
        arr = sorted(list(hash.keys()))
        
        for num in arr:
            curr = max(curr+num, num)
            ret = max(curr, ret)

        return ret