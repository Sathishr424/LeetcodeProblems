# Last updated: 28/10/2025, 1:18:01 am
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            for d in str(num):
                ret.append(int(d))

        return ret