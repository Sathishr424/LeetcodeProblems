# Last updated: 3/7/2025, 5:40:05 pm
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10 ** 9 + 7
        # aabbccdd
        # abccdd

        # aa dd
        # aadd, aad, ad, add

        freq_cnt = []
        n = len(word)
        cnt = 1
        for i in range(1, n):
            if word[i] != word[i-1]:
                freq_cnt.append(cnt)
                cnt = 1
            else:
                cnt += 1
        
        freq_cnt.append(cnt)
        freq_cnt.sort()
        m = len(freq_cnt)
        prefix = [1] * (m + 2)
        for i in range(m-1, -1, -1):
            prefix[i] = prefix[i + 1] * freq_cnt[i] % mod
        # print(freq_cnt)
        # print(prefix)
        # print(m)
        @cache
        def rec(index, rem):
            if rem == 0:
                # print(index)
                return prefix[index]
            if index == m: return 0

            ans = 0
            for cnt in range(1, min(rem, freq_cnt[index]) + 1):
                curr = rec(index + 1, rem - cnt)
                if rem-cnt == 0:
                    curr *= freq_cnt[index] - cnt + 1
                    curr %= mod
                ans += curr
                ans %= mod
            return ans

        ans = rec(0, k)
        rec.cache_clear()
        return ans