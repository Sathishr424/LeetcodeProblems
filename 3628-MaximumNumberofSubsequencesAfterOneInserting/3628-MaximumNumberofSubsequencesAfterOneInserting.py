# Last updated: 28/7/2025, 6:00:33 pm
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        # s = ''.join([chr(random.randrange(26) + 97) for _ in range(10**5)])
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

        # print(prefix_l)
        # print(suffix_t)

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
        
        # print(ret, cnt)
        ret = max(ret, cnt)

        @cache
        def rec(index, added):
            if index == n: return 0

            ans = 0
            if not added:
                ans = prefix_l[index] * suffix_t[index] + rec(index, True)
            
            if s[index] == 'C':
                ans = max(ans, prefix_l[index] * suffix_t[index] + rec(index + 1, added))
            else:
                ans = max(ans, rec(index + 1, added))
            return ans

        return max(ret, rec(0, False))