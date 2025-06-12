# Last updated: 12/6/2025, 5:52:11 am
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1

        while l < r:
            t = numbers[l] + numbers[r]
            if t > target:
                r -= 1
            elif t < target:
                l += 1
            else:
                return [l+1, r+1]
        return []