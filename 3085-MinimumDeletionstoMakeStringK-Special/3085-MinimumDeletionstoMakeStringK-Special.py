# Last updated: 21/6/2025, 9:14:20 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # bbbcc
        # 4-2 = 2

        freq = defaultdict(int)
        for char in word:
            freq[char] += 1
        
        # [3, 4, 2, 6, 4]
        # [2, 3, 4, 4, 6]
        # [2, 3, 2, 3, 4]

        arr = sorted(list(freq.values()))
        # print(arr)

        @cache
        def rec(l, r):
            if l == r: return 0

            diff = arr[r] - arr[l]
            if diff > k:
                return min(rec(l+1, r) + arr[l], rec(l, r-1) + max(0, arr[r] - arr[l] - k))
            else:
                return 0
        
        return rec(0, len(arr)-1)