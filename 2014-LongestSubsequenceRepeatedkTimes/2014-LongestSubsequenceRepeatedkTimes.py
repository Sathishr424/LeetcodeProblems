# Last updated: 27/6/2025, 9:28:04 pm
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # aabacc
        # s = 'a' * (10 ** 4)
        n = len(s)

        freq = [0] * 26
        for i in range(n):
            freq[ord(s[i]) - 97] += 1

        ret = 0
        curr = [0] * 26

        def rec(start, index):
            nonlocal ret
            # print(start, index)
            if index == n: return

            a = ord(s[index]) - 97
            if freq[a] >= k:
                curr[a] += 1
                new_start = min(start, index)
                cnt = 0
                for i in range(26):
                    if curr[i] >= k:
                        cnt += curr[i]
                if cnt == index - new_start + 1:
                    ret = max(ret, index - new_start + 1)

                rec(new_start, index + 1)
                curr[a] -= 1
            if start == n:
                rec(start, index + 1)

        rec(n, 0)
        
        return ret