# Last updated: 16/7/2025, 11:38:20 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def maximumLength(self, nums: List[int], k) -> int:
        n = len(nums)

        ret = 0
        for match in range(k):
            counter = [0] * k
            for i in range(n):
                need = (k - (nums[i] % k) - match) % k

                counter[nums[i] % k] = cmax(1, counter[need] + 1)
                ret = cmax(counter[nums[i] % k], ret)
        
        return ret