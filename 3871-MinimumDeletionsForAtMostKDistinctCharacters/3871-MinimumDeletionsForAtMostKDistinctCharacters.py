# Last updated: 12/6/2025, 5:33:17 am
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        arr = sorted(freq.values(), reverse=True)
        ret = 0
        while len(arr) > k:
            ret += arr.pop()

        return ret