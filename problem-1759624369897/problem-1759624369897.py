# Last updated: 5/10/2025, 6:02:49 am
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        best = inf
        for i in range(n):
            if words[i] == target:
                best = min(best, (i - startIndex) % n, (startIndex - i) % n)

        return -1 if best == inf else best