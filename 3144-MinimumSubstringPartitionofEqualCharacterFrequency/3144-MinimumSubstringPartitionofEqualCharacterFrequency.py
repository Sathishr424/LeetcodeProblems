# Last updated: 7/7/2025, 9:08:26 pm
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        inf = float('inf')
        def charToInt(a):
            return ord(a) - ord('a')
        
        @cache
        def rec(index):
            if index == n: return 0

            freq = [0] * 26
            max_freq = 0
            cnt = 0
            ans = inf

            for i in range(index, n):
                a = charToInt(s[i])
                freq[a] += 1
                if freq[a] == 1: cnt += 1
                if freq[a] > max_freq:
                    max_freq += 1
                if max_freq * cnt == (i - index + 1):
                    # print((index, i), max_freq, cnt)
                    ans = min(ans, rec(i + 1) + 1)
                # print('check', (index, i), cnt, max_freq)
            return ans
        
        ans = rec(0)
        rec.cache_clear()
        return ans