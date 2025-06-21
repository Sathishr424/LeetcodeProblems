# Last updated: 21/6/2025, 10:45:44 am
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
            for j in range(n-1, i, -1):
                diff = arr[j] - arr[i]
                if diff > k:
                    best += diff - k
                else: 
                    break
            ret = min(ret, best)
            p += arr[i]

        return ret