# Last updated: 21/6/2025, 10:51:50 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        arr = sorted(Counter(word).values())
        n = len(arr)
        ret = len(word)
        p = 0
        for i in range(n):
            best = p
            for j in range(n-1, i, -1):
                diff = arr[j] - arr[i]
                if diff > k:
                    best += diff - k
                else: break
            ret = min(ret, best)
            p += arr[i]

        return ret