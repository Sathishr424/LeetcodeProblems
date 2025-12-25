# Last updated: 12/25/2025, 7:08:30 PM
class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)

        best = 'z' * (n + 1)
        for i in range(1, n+1):
            left = s[:i][::-1] + s[i:]
            right = s[:n-i] + s[n-i:][::-1]
            best = min(best, left, right)

        return best