# Last updated: 21/6/2025, 9:15:41 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        for char in word:
            freq[char] += 1

        arr = sorted(list(freq.values()))

        @cache
        def rec(l, r):
            if l == r: return 0

            diff = arr[r] - arr[l]
            if diff > k:
                return min(rec(l+1, r) + arr[l], rec(l, r-1) + diff - k)
            else:
                return 0
        
        return rec(0, len(arr)-1)