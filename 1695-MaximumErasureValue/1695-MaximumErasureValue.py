# Last updated: 22/7/2025, 2:58:21 pm
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        freq = defaultdict(int)
        prev = 0
        ret = nums[0]
        s = 0

        for i in range(n):
            while freq[nums[i]]:
                freq[nums[prev]] -= 1
                s -= nums[prev]
                prev += 1
            freq[nums[i]] += 1
            s += nums[i]
            ret = max(ret, s)
        
        return ret