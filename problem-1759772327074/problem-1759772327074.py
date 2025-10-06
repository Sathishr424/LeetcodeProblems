# Last updated: 6/10/2025, 11:08:47 pm
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor