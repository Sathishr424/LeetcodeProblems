# Last updated: 25/10/2025, 8:03:50 pm
class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)

        best = 'z' * (n + 1)
        for i in range(1, n+1):
            left = s[:i][::-1] + s[i:]
            right = s[:n-i] + s[n-i:][::-1]
            best = min(best, left, right)

        return best