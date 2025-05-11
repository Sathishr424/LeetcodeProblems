# Last updated: 11/5/2025, 10:27:37 am
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        ret = 0
        for char in freq:
            cnt = freq[char]
            while cnt >= 3:
                cnt -= 2
            ret += cnt
        
        return ret