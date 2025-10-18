# Last updated: 18/10/2025, 2:18:57 pm
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        prev = nums[0] - k
        used = set()
        used.add(prev)

        for i in range(1, n):
            if nums[i] - k <= prev:
                num = min(nums[i] + k, prev + 1)
            else:
                num = nums[i] - k
            prev = num
            used.add(prev)
        
        return len(used)