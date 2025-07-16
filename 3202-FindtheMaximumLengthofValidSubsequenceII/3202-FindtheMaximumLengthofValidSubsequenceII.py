# Last updated: 16/7/2025, 11:39:31 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def maximumLength(self, nums: List[int], k) -> int:
        n = len(nums)

        ret = 0
        for match in range(k):
            counter = [0] * k
            for i in range(n):
                need = (k - (nums[i] % k) - match) % k
                curr = nums[i] % k
                counter[curr] = cmax(1, counter[need] + 1)
                ret = cmax(counter[curr], ret)
        
        return ret