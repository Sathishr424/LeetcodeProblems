# Last updated: 5/10/2025, 6:02:11 am
class Solution:
    def closestTarget(self, words: List[str], target: str, index: int) -> int:
        n = len(words)

        best = inf
        for i in range(n):
            if words[i] == target:
                best = min(best, abs(i - index))

                j = index
                if j > i:
                    i, j = j, i

                best = min(best, j + (n - i))

        return -1 if best == inf else best