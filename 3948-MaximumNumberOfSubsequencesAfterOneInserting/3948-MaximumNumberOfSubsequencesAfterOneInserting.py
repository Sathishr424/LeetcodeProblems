# Last updated: 12/25/2025, 7:10:26 PM
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        
        prefix_l = [0] * n
        suffix_t = [0] * n
        t = 0

        for i in range(n-1, -1, -1):
            if s[i] == 'T':
                t += 1
            suffix_t[i] = t
        
        l = 0
        for i in range(n):
            if s[i] == 'L':
                l += 1
            prefix_l[i] = l

        ret = 0
        l_cnt = 1
        cnt = 0
        for i in range(n):
            if s[i] == 'L':
                l_cnt += 1
            elif s[i] == 'C':
                cnt += l_cnt * suffix_t[i]
        
        ret = cnt
        cnt = 0
        t_cnt = 1
        for i in range(n-1, -1, -1):
            if s[i] == 'T':
                t_cnt += 1
            elif s[i] == 'C':
                cnt += t_cnt * prefix_l[i]
        
        ret = max(ret, cnt)

        dp = [[-1, -1] for _ in range(n + 1)]
        dp[n] = [0, 0]
        
        def rec(index, added):
            if dp[index][added] != -1: return dp[index][added]

            ans = 0
            if not added:
                ans = prefix_l[index] * suffix_t[index] + rec(index, True)
            
            if s[index] == 'C':
                ans = max(ans, prefix_l[index] * suffix_t[index] + rec(index + 1, added))
            else:
                ans = max(ans, rec(index + 1, added))
            dp[index][added] = ans
            return ans

        return max(ret, rec(0, False))