# Last updated: 8/1/2026, 10:57:17 PM
1class Solution:
2    def predictTheWinner(self, nums: List[int]) -> bool:
3        tot = sum(nums)
4        @cache
5        def rec(l, r, p1_s, p1_turn):
6            if l > r:
7                return p1_s >= tot - p1_s
8            if p1_turn:
9                return rec(l+1, r, p1_s + nums[l], not p1_turn) or rec(l, r-1, p1_s + nums[r], not p1_turn)
10            else:
11                return rec(l+1, r, p1_s, not p1_turn) and rec(l, r-1, p1_s, not p1_turn)
12        
13        ans = rec(0, len(nums)-1, 0, True)
14        rec.cache_clear()
15        return ans