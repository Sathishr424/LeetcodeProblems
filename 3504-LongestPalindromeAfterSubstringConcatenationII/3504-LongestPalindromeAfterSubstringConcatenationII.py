# Last updated: 26/6/2025, 11:48:50 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        tot = n + m
        st = s + t
        ret = 1
        
        def rec_left(i, j):
            if i < 0 or j == tot: return 0

            ans = rec_left(i-1, j)

            if st[i] == st[j]:
                cnt = 0
                while i >= 0 and j < tot and st[i] == st[j]:
                    i -= 1
                    j += 1
                    cnt += 2
                ans = cmax(ans, cnt)
            
            return ans
        
        def rec_right(i, j):
            if i < 0 or j == tot: return 0

            ans = rec_right(i, j + 1)

            if st[i] == st[j]:
                cnt = 0
                while i >= 0 and j < tot and st[i] == st[j]:
                    i -= 1
                    j += 1
                    cnt += 2
                ans = cmax(ans, cnt)
            
            return ans

        def do_left(left, right):
            cnt = rec_left(n-1, right + 1)
            return right - left + cnt + 1
        
        def do_right(left, right):
            cnt = rec_right(left - 1, n)
            return right - left + cnt + 1

        for i in range(1, tot):
            left = i-1
            right = i
            while left >= 0 and right < tot and st[left] == st[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            ret = cmax(ret, right - left + 1)
            if left >= n:
                ret = cmax(ret, do_left(left, right))
            if right < n:
                ret = cmax(ret, do_right(left, right))
            
            left = i-1
            right = i+1
            while left >= 0 and right < tot and st[left] == st[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            ret = cmax(ret, right - left + 1)

            if left >= n:
                ret = cmax(ret, do_left(left, right))
            if right < n:
                ret = cmax(ret, do_right(left, right))

        return ret