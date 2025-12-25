# Last updated: 12/25/2025, 7:08:32 PM
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnts = Counter(nums)
        s = 0
        for num in cnts:
            if cnts[num] % k == 0:
                s += num * cnts[num]

        return s