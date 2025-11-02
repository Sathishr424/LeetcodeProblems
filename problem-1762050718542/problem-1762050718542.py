# Last updated: 2/11/2025, 8:01:58 am
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