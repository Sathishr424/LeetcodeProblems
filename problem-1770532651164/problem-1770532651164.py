# Last updated: 2/8/2026, 12:07:31 PM
1class Solution:
2    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
3        m = len(nums1)
4        n = len(nums2)
5
6        @cache
7        def rec(i, j, rem):
8            if rem == 0: return 0
9            if i == m or j == n: return -inf
10
11            return max(rec(i+1, j, rem), rec(i, j+1, rem), rec(i+1, j+1, rem - 1) + nums1[i] * nums2[j])
12
13        ans = rec(0, 0, k)
14        rec.cache_clear()
15        return ans
16        