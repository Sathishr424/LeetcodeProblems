# Last updated: 12/6/2025, 5:34:11 am
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # s = 'a' * 32
        # t = 'b' * 32
        
        m = len(s)
        n = len(t)

        left = []
        ret = 1

        for s_l in range(m):
            for s_r in range(m, s_l, -1):
                curr = s[s_l:s_r]
                if curr == curr[::-1]:
                    ret = max(ret, len(curr))
                left.append(curr)
        right = []
        for t_l in range(n):
            for t_r in range(n, t_l, -1):
                curr = t[t_l:t_r]
                if curr == curr[::-1]:
                    ret = max(ret, len(curr))
                right.append(curr)

        for st in left:
            for ts in right:
                curr = st+ts
                # print(curr)
                if curr == curr[::-1]:
                    ret = max(ret, len(curr))
        # print(left)
        # print(right)
        return ret
                

        
            