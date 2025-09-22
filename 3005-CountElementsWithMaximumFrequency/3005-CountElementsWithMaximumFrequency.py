# Last updated: 22/9/2025, 12:50:17 pm
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = len(nums)

        max_freq = 0
        freq = [0] * 101
        for num in nums:
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
        
        count = 0
        for num in nums:
            if freq[num] == max_freq:
                count += 1
        
        return count