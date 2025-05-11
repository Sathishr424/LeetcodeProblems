# Last updated: 11/5/2025, 10:20:51 am
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        arr = sorted(freq.values(), reverse=True)
        cnt = sum(freq.values())
        ret = 0
        while len(arr) > k:
            ret += arr.pop()

        return ret