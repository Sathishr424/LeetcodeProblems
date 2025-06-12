# Last updated: 12/6/2025, 5:49:45 am
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ret = 0
        vis = {}
        for i in s:
            if i in vis: continue
            vis[i] = 1
            cnt = s.count(i)
            if cnt // 2 >= 1:
                ret += cnt - (cnt%2)
            if ret % 2 == 0: ret += (cnt%2)
        return ret