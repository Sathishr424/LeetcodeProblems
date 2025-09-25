# Last updated: 26/9/2025, 2:19:12 am
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # a + (c * space) = b
        # (a + b) / space = c
        # (a + b) % space = 0
        if space == 1: return min(nums)
        n = len(nums)
        r_nums = nums[:]

        there = defaultdict(int)
        for i in range(n):
            nums[i] %= space
            there[nums[i]] += 1

        best = 0
        best_index = 0
        for i in range(n):
            cnt = there[nums[i]]

            if cnt > best or (cnt == best and r_nums[i] < r_nums[best_index]):
                best = cnt
                best_index = i

        return r_nums[best_index]        