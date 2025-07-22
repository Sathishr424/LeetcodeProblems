# Last updated: 22/7/2025, 3:01:26 pm
N = 10**4 + 1
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        freq = [0] * N
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
            if s > ret: ret = s
        
        return ret