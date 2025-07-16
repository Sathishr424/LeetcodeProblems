# Last updated: 16/7/2025, 12:27:09 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maximumLength(self, nums: List[int], k) -> int:
        n = len(nums)

        ret = 0
        for match in range(k):
            counter = [0] * k
            for i in range(n):
                curr = nums[i] % k
                need = (match - curr) % k
                counter[curr] = cmax(1, counter[need] + 1)
                ret = cmax(counter[curr], ret)
        
        return ret