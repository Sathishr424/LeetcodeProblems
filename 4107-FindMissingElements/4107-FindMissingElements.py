# Last updated: 12/25/2025, 7:08:11 PM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        there = set(nums)
        nums.sort()

        l = nums[0]
        r = nums[-1]

        ret = []
        for i in range(l + 1, r):
            if i not in there:
                ret.append(i)

        return ret