# Last updated: 12/25/2025, 7:09:23 PM
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        nums.sort()

        ret = []
        used = {}
        while k and nums:
            num = nums.pop()
            if num in used: continue
            ret.append(num)
            used[num] = 1
            k -= 1

        return ret