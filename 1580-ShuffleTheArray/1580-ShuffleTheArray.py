# Last updated: 12/6/2025, 5:41:24 am
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[n+i])
        return ret