# Last updated: 12/10/2025, 8:01:25 am
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnts = Counter(nums)
        s = 0
        for num in cnts:
            if cnts[num] % k == 0:
                s += num * cnts[num]

        return s