# Last updated: 11/11/2025, 1:57:23 pm
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        sizes = []
        
        for i in range(N):
            one = strs[i].count('1')
            zero = len(strs[i]) - one
            sizes.append((one, zero))
        
        @cache
        def rec(index, rem_m, rem_n):
            if index == N:
                return 0
            
            one = sizes[index][0]
            zero = sizes[index][1]

            ans = rec(index + 1, rem_m, rem_n)
            if rem_m >= zero and rem_n >= one:
                ans = max(ans, rec(index + 1, rem_m - zero, rem_n - one) + 1)
            
            return ans
        
        ans = rec(0, m, n)
        rec.cache_clear()
        return ans