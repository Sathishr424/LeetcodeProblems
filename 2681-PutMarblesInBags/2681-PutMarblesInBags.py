# Last updated: 12/6/2025, 5:37:17 am
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        if k == n: return 0
        prefix = []
        for i in range(1, n):
            prefix.append(weights[i-1]+weights[i])

        prefix.sort()
        k -= 1
        n -= 1
        return sum(prefix[n-k:]) - sum(prefix[:k])





