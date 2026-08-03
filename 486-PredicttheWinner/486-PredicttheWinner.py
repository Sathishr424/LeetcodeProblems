# Last updated: 8/3/2026, 7:21:14 PM
1class Solution:
2    def predictTheWinner(self, nums: List[int]) -> bool:
3        n = len(nums)
4
5        @cache
6        def rec(l, r, score, turn):
7            if l > r:
8                return 1 if score >= 0 else -1
9
10            add = 1 if turn else -1
11            left = rec(l+1, r, score + nums[l] * add, not turn)
12            right = rec(l, r-1, score + nums[r] * add, not turn)
13
14            return max(left, right) if turn else min(left, right)
15
16        ans = rec(0, n-1, 0, True)
17        rec.cache_clear()
18        return ans >= 0