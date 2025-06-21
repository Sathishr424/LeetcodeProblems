# Last updated: 21/6/2025, 10:47:07 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - 97] += 1

        arr = sorted([freq[i] for i in range(26) if freq[i]])
        n = len(arr)
        ret = 100001
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