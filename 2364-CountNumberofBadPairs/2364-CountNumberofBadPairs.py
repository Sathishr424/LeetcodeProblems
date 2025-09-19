# Last updated: 19/9/2025, 11:45:46 pm
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        freq = defaultdict(int)
        for i, num in enumerate(nums):
            freq[num - i] += 1
        
        total = n * (n - 1) // 2

        for num in freq:
            total -= freq[num] * (freq[num] - 1) // 2
        
        return total