# Last updated: 10/5/2025, 9:38:54 pm
vowels = 'aeiou'

class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0] * 26
        x = 0
        y = 0

        for char in s:
            num = ord(char) - 97
            freq[num] += 1
            if char in vowels:
                y = max(y, freq[num])
            else:
                x = max(x, freq[num])

        return x+y