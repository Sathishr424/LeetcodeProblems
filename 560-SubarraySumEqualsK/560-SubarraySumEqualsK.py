# Last updated: 25/4/2025, 3:53:38 pm
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        s = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for i in range(n):
            s += nums[i]

            ret += prefix[s-k]
            prefix[s] += 1
        
        return ret