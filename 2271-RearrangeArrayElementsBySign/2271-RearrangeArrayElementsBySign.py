# Last updated: 12/6/2025, 5:38:36 am
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 0
        ret = [0] * len(nums)
        for num in nums:
            if num < 0:
                ret[(neg*2)+1] = num
                neg += 1
            else:
                ret[pos*2] = num
                pos += 1
        return ret