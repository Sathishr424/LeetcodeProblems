# Last updated: 12/25/2025, 7:09:21 PM
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        op = 0
        for i in range(1, 26):
            if freq[i]:
                op += 1
                freq[(i + 1) % 26] += freq[i]

        return op