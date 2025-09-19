# Last updated: 19/9/2025, 10:47:46 pm

N = 10**9 + 1
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # nums = [random.randrange(1, N) for _ in range(10 ** 5)]
        n = len(nums)
        if n == 1: return 0
        
        prev = nums[-1]
        op = 0
        for i in range(n-2, -1, -1):
            if nums[i] > prev:
                steps = (nums[i] - 1) // prev
                prev = nums[i] // (steps + 1)
                op += steps
            else:
                prev = nums[i]
        
        return op