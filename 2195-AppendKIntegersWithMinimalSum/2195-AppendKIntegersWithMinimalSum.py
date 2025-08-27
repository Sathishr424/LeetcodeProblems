# Last updated: 27/8/2025, 10:12:46 pm
cmin = lambda x, y: x if x < y else y
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        prev = 0
        for i in range(len(nums)):
            if nums[i] == prev: continue
            diff = cmin(nums[i] - prev - 1, k)
            total += prev * diff + (diff * (diff + 1) // 2)
            k -= diff
            if k == 0: return total
            prev = nums[i]

        total += prev * k + (k * (k + 1) // 2)
        return total