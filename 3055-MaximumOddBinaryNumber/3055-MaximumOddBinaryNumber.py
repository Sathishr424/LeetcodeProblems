# Last updated: 12/6/2025, 5:36:20 am
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = 0
        for c in s:
            ones += c == '1'
        ones -= 1
        return (ones * '1') + ('0' * (n-ones-1)) + '1'