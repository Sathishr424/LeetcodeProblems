# Last updated: 21/4/2025, 5:59:36 pm
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)

        m = n+1
        vis = [True] * (m+1)
        max_ans = '9' * m

        def rec(index, st, prev):
            if index == m: return st
            ans = max_ans
            if pattern[index-1] == 'I':
                l = prev+1
                r = m+1
            else:
                l = 1
                r = prev
            for i in range(l, r):
                if vis[i]:
                    vis[i] = False
                    ans = min(ans, rec(index+1, st+str(i), i))
                    vis[i] = True
            return ans
        
        ans = max_ans
        for i in range(1, m+1):
            vis[i] = False
            ans = min(ans, rec(1, str(i), i))
            vis[i] = True
        return ans