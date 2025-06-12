# Last updated: 12/6/2025, 5:44:22 am
class Solution:
    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        half = total / 3

        if half != total//3: return False
        index = 0
        left = 0
        for i in range(n):
            left += nums[i]
            index += 1
            if left == half:
                break

        if left < half or left > half: return False

        left = 0
        for j in range(i+1, n):
            left += nums[j]
            index += 1
            if left == half:
                break

        if left < half or left > half: return False

        return index < n
