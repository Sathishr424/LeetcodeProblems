# Last updated: 13/9/2025, 2:48:52 pm
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = defaultdict(int)
        max_v = 0
        max_c = 0
        for char in s:
            freq[char] += 1
            if char in 'aeiou':
                if freq[char] > max_v:
                    max_v = freq[char]
            elif freq[char] > max_c:
                max_c = freq[char]
        
        return max_c + max_v