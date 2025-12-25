# Last updated: 12/25/2025, 7:08:44 PM
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        def isBalanced(freq):
            prev = -1
            for char in freq:
                cnt = freq[char]
                if prev != -1 and cnt != prev: return False
                prev = cnt
            
            return True

        best = 1
        for i in range(n):
            cnt = 0
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1
                if isBalanced(freq):
                    best = max(best, j - i + 1)

        return best
                    