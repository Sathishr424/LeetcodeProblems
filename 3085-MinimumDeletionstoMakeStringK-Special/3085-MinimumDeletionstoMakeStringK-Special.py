# Last updated: 21/6/2025, 10:50:50 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        arr = sorted(Counter(word).values())
        n = len(arr)
        ret = len(word)
        p = 0
        for i in range(n):
            best = p
            j = n-1
            while j > i and arr[j] - arr[i] > k:
                best += arr[j] - arr[i] - k
                j -= 1
            ret = min(ret, best)
            p += arr[i]

        return ret