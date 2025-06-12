# Last updated: 12/6/2025, 5:39:17 am
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])

        dp = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                cnt = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        cnt += 1
                dp[i][j] = cnt

        @cache
        def rec(i, mask):
            if i == m: return 0
            ans = 0
            for j in range(m):
                if not mask & (1<<j):
                    ans = max(ans, rec(i+1, mask ^ (1<<j)) + dp[i][j])
            
            return ans

        return rec(0, 1<<m)
            
                    
