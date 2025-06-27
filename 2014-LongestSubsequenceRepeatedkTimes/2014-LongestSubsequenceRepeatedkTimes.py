# Last updated: 27/6/2025, 9:44:47 pm
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # aabacc
        # s = 'a' * (10 ** 4)
        n = len(s)

        freq = [0] * 26
        for i in range(n):
            freq[ord(s[i]) - 97] += 1

        ret = 0
        prev = 0
        curr = [0] * 26

        def checkWindow(index, curr):
            nonlocal ret
            if index - prev <= ret: return
            for j in range(prev, index):
                a = ord(s[j]) - 97
                cnt = 0
                for i in range(26):
                    if curr[i] >= k:
                        cnt += curr[i]
                if cnt == index - j:
                    ret = max(ret, cnt)
                    break
                
                curr[a] -= 1

        for i in range(n):
            a = ord(s[i]) - 97
            if freq[a] >= k:
                curr[a] += 1
                checkWindow(i + 1, curr[:])
            else:
                for j in range(prev, i):
                    curr[ord(s[j]) - 97] -= 1
                prev = i + 1
        
        return ret